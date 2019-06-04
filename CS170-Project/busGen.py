#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 18:18:51 2018

@author: alexkern
"""

from mosek.fusion import *
import sys
import networkx as nx
import os
import numpy as np
import matplotlib.pyplot as plt
import mosek



# Define a stream printer to grab output from MOSEK
def streamprinter(text):
    sys.stdout.write(text)
    sys.stdout.flush()



def busOpt(userGraph, busMax, time):
    ''' Using quadratic optimiaxation with integer objectives, this function returns a good estimate
    for any bus. 
    
    Params:
        userGraph   - This is the graph of the remaining students. we dont know how many exist however
        there must be at least one or it WILL return an error
        
        busMax      - Caculated beforehand, it should either be the size of the bus, or how many students could be
        put on the bus such that a feasable solution still exists. Used as a constraint on the objective
        
        time        - This is so larger sets can be calcualted in a more feasable amount of space. puts constraints
        on the solver so it does not take to long. 
    
    '''
    
    
    '''
    create a mapping for the nodes of the bus so calculations are a bit less intense each time
    '''
    #maps each to a specific num
    mapping = dict(zip(userGraph.nodes(),list(range(nx.number_of_nodes(userGraph)))))
    #reversMap is for the return value. 
    reverseMap = dict(zip(list(range(nx.number_of_nodes(userGraph))),userGraph.nodes()))
    #copies and does not modify inputs
    G = nx.relabel_nodes(userGraph,mapping, copy=True)
    
    H = np.array(nx.to_numpy_matrix(G))
    n = len(H)
    for i in range(n):
        H[i][i] = -n*2

    with mosek.Env() as env:
        # Attach a printer to the environment
        #env.set_Stream(mosek.streamtype.log, streamprinter)
        # Create a task object
        with env.Task() as task:
            # Attach a log stream printer to the task
            #task.set_Stream (mosek.streamtype.log, streamprinter)
            
            # numvar is equal to n in the nxn matrix H
            numvar = n
            '''
            For each bound, we need to define it in the array.
            each begins with mosek.boundkey.(insert postfix here)
            the endings are as follows:
                ra  -- at position i in the array if ra is the postfix, than blc[i] <= Ax[i] <= buc[i]
                fx  -- at position i in the array if fx is the postfix, than Ax[i] = blc[i]
                fr  -- at position i in the array if fr is the postfix, than -inf <= Ax[i] <= inf
                lo  -- at position i in the array if fr is the postfix, than blc[i] <= Ax[i] <= inf
                up  -- at position i in the array if fr is the postfix, than -inf <= Ax[i] <= buc[i]
            Note that we define A later. In the following case A is a 1xn matrix with lowerbound 1.0 and
            upperbound 5.0
            '''
            bkc = [mosek.boundkey.ra]
            blc = [1.0] #At least 1 kid on the bus
            buc = [busMax] #bus size
            '''
            This is where the matrix A is created, it must follow the constriants in order as provided above.
            Note in this case:
                A = [1, 1, ... , 1, 1]
            This is becase on asub each sub-array is a list, and on that list is the places below the column
            where there exists variables. Each corresponding aval is the value of that item.
            I assume this is so mosek can optimize sparce data.
            '''
            asub = [[0] for i in range(n)]
            aval = [[1.0] for i in range(n)]
            '''
            This should be a little more straigtforward. We set the constriants on the variable itself,
            saying any xi is such that 0.0 <= xi <= 1.0  for all x. When we declare it an integer func
            this ensures each xi is either 0 or 1. Not much modification should happen here unless we decide
            to do two busses at once
            '''
            bkx = [mosek.boundkey.ra] * numvar 
            blx = [0.0] * numvar
            bux = [1.0] * numvar
            
            '''
            Our objective function is as follows:
                (0.5)x.T*H*x + c.T*x
            To ensure negative semidefinate, we needed to make the diagonal of H -2*n for each entry.
            This way we could maximize the problem, however the results needed to be fixed so adding a 
            linear objective which adds the values back which otherwise would have been subtracted off.
            Making each value of c[i] == n fixed this issue.
            '''
            c = [n for i in range(n)]
            
            '''
            now we need to add the number of constraints to the problem.
            '''
            numcon = len(bkc)
            
            # Append 'numcon' empty constraints.
            # The constraints will initially have no bounds.
            task.appendcons(numcon)

            # Append 'numvar' variables.
            # The variables will initially be fixed at zero (x=0).
            task.appendvars(numvar)
        
            for j in range(numvar):
                # Set the linear term c_j in the objective.
                task.putcj(j, c[j])
                # Set the bounds on variable j
                # blx[j] <= x_j <= bux[j]
                task.putbound(mosek.accmode.var, j, bkx[j], blx[j], bux[j])
                # Input column j of A
                # Variable (column) index. # Row index of non-zeros in column j.
                task.putacol(j, asub[j], aval[j])            # Non-zero Values of column j.
            for i in range(numcon):
                task.putbound(mosek.accmode.con, i, bkc[i], blc[i], buc[i])
            
            # Set up and input quadratic objective
            qsubi = []
            qsubj = []
            qval = []
            for i in range(n):
                for j in range(0, i+1):
                    if H[i][j] != 0:
                        qsubi.append(i)
                        qsubj.append(j)
                        qval.append(H[i][j])
            #print(qsubi)
            #print(qsubj)
            #print(qval)
            task.putqobj(qsubi, qsubj, qval)
            
            # Input the objective sense (minimize/maximize)
            task.putobjsense(mosek.objsense.maximize)
            # Define variables to be integers
            task.putvartypelist([i for i in range(n)],[mosek.variabletype.type_int for i in range(n)])
            
            
            # Set max solution time 
            task.putdouparam(mosek.dparam.mio_max_time, time);
            # Optimize
            task.optimize()
            # Print a summary containing information
            # about the solution for debugging purposes
            task.solutionsummary(mosek.streamtype.msg)
            
            prosta = task.getprosta(mosek.soltype.itg)
            solsta = task.getsolsta(mosek.soltype.itg)

            # Output a solution
            xx = [0.] * numvar
            task.getxx(mosek.soltype.itg, xx)
            solSet = []
#            tempSol = []
            
            '''
            This is what we will return for each bus, fixed and all
            '''
            for i in range(len(xx)):
                if xx[i] > 0.5:
                    solSet += [reverseMap[i]]
#            print(solSet)
#            print(tempSol)
            if solsta in [mosek.solsta.integer_optimal, mosek.solsta.near_integer_optimal]:
                print("Optimal solution: %s" % xx)
            elif solsta == mosek.solsta.dual_infeas_cer:
                print("Primal or dual infeasibility.\n")
            elif solsta == mosek.solsta.prim_infeas_cer:
                print("Primal or dual infeasibility.\n")
            elif solsta == mosek.solsta.near_dual_infeas_cer:
                print("Primal or dual infeasibility.\n")
            elif solsta == mosek.solsta.near_prim_infeas_cer:
                print("Primal or dual infeasibility.\n")
            elif mosek.solsta.unknown:
                if prosta == mosek.prosta.prim_infeas_or_unbounded:
                    print("Problem status Infeasible or unbounded.\n")
                elif prosta == mosek.prosta.prim_infeas:
                    print("Problem status Infeasible.\n")
                elif prosta == mosek.prosta.unkown:
                    print("Problem status unkown.\n")
                else:
                    print("Other problem status.\n")
            else:
                print("Other solution status (good)")
            v = np.array(xx)
            print(v.dot(H).dot(v)*.5 + v.dot(c))
            return solSet