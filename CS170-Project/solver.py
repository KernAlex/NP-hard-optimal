import networkx as nx
import os
from rowdy_kids import rowdyKidSplitter
import random
import busGen as bg
import numpy


###########################################
# Change this variable to the path to 
# the folder containing all three input
# size category folders
###########################################
path_to_inputs = "./all_inputs"

###########################################
# Change this variable if you want
# your outputs to be put in a 
# different folder
###########################################
path_to_outputs = "./outputs"

###########################################
#For splitting up buses
 
def partition (list_in, n):
    random.shuffle(list_in)
    return [list_in[i::n] for i in range(n)]

def parse_input(folder_name):
    '''
        Parses an input and returns the corresponding graph and parameters

        Inputs:
            folder_name - a string representing the path to the input folder

        Outputs:
            (graph, num_buses, size_bus, constraints)
            graph - the graph as a NetworkX object
            num_buses - an integer representing the number of buses you can allocate to
            size_buses - an integer representing the number of students that can fit on a bus
            constraints - a list where each element is a list vertices which represents a single rowdy group
    '''
    graph = nx.read_gml(folder_name + "/graph.gml")
    parameters = open(folder_name + "/parameters.txt")
    num_buses = int(parameters.readline())
    size_bus = int(parameters.readline())
    constraints = []
    
    for line in parameters:
        line = line[1: -2]
        curr_constraint = [num.replace("'", "") for num in line.split(", ")]
        constraints.append(curr_constraint)

    return graph, num_buses, size_bus, constraints

def solve(graph, num_buses, size_bus, constraints):
    setOfBuses = []
    rowdyBus = rowdyKidSplitter(constraints)



    #remove kids from graph
    for i in rowdyBus:
        graph.remove_node(i)
    
    
    '''
    Two conditions apply here. Is rowdy bus of the right size? if not fix it.
    now we ensure that the remaining graph fits the rest of the busses maximally
    by splitting them up into other busses.
    It may be the case where we need to take the rowdybus and put them in more 
    optimal positions. do that first than optimize
    '''
    
    random.shuffle(rowdyBus)
    rowdyBusNum = int(len(rowdyBus) / size_bus)
    #fill in busses before tail case
    for i in range(rowdyBusNum):
        
        setOfBuses.append(rowdyBus[i*size_bus:(i+1)*size_bus])
       
    #tail case
    tail = []
    if rowdyBus[rowdyBusNum*size_bus:]:
        tail = rowdyBus[rowdyBusNum*size_bus:]
    '''
    len(rowdyBus) + graph.number_of_nodes() = Total kids
    if graph.number_of_nodes()/size_bus > num_busses - (tail + len(setOfBusses)):
        fill up each remaining bus with size_bus, put remaing students in tail,
        append tail
    else if graph.number_of_nodes()/size_bus = num_busses - (tail + len(setOfBusses)):
        fill up each remaning bus with size_bus, append tail, you're done
    else:
        disperse the rowdy students amongst the busses until you get optimal num.
    '''
    l = 0
    if len(tail) > 0:
        l = 1
    if graph.number_of_nodes()/size_bus > num_buses - (l+len(setOfBuses)):
        print("GREATER THAN")
        for i in range(num_buses - (len(setOfBuses) + l)):
            tempBus = bg.busOpt(graph, size_bus, 7)
            setOfBuses.append(tempBus)
            for i in tempBus:
                graph.remove_node(i)
        tail += list(graph.nodes())
    elif graph.number_of_nodes()/size_bus == num_buses - (l + len(setOfBuses)):
        print("EQUALS")
        for i in range(num_buses - (len(setOfBuses) + l)):
            tempBus = bg.busOpt(graph, size_bus, 7)
            setOfBuses.append(tempBus)
            for i in tempBus:
                graph.remove_node(i)
            busesLeft = num_buses - len(setOfBuses)
            
        
    else:
        print("ELSE OH NO")
        tail = []
        setOfBuses = partition(rowdyBus, min(len(rowdyBus), num_buses - int(graph.number_of_nodes()/size_bus) - l ))
        for i in range(num_buses - (len(setOfBuses)) - 1):
            tempBus = bg.busOpt(graph, size_bus, 7)
            setOfBuses.append(tempBus)
            for i in tempBus:
                graph.remove_node(i)
            busesLeft = num_buses - len(setOfBuses)
            if graph.number_of_nodes() - size_bus <= busesLeft:
                FinishHim = list(graph.nodes())
                random.shuffle(FinishHim)
                Fatality = partition(FinishHim, busesLeft)
                setOfBuses += Fatality
                for i in FinishHim:
                    graph.remove_node(i)
                break
                
        tail += list(graph.nodes())

    if tail:
        setOfBuses.append(tail)
    print(len(setOfBuses))

    bigset =[]
    for set in setOfBuses:
        if len(set) > size_bus:
            bigset = set

    while(len(bigset) > size_bus):
        for bus in setOfBuses:
            while (len(bus) < size_bus and len(bigset) > size_bus):
                extra = set.pop()
                bus.append(extra)
    return setOfBuses

def main():
    '''
        Main method which iterates over all inputs and calls `solve` on each.
        The student should modify `solve` to return their solution and modify
        the portion which writes it to a file to make sure their output is
        formatted correctly.
    '''

    size_categories = ["medium"] #, "medium", "large"]
    if not os.path.isdir(path_to_outputs):
        os.mkdir(path_to_outputs)

    for size in size_categories:
        category_path = path_to_inputs + "/" + size
        output_category_path = path_to_outputs + "/" + size
        category_dir = os.fsencode(category_path)
        
        if not os.path.isdir(output_category_path):
            os.mkdir(output_category_path)

        for input_folder in os.listdir(category_dir):
            input_name = os.fsdecode(input_folder) 
            if input_name == ".DS_Store":
                continue

# #            if input_name != "2a` 02":
# #                continue
#
            if input_name != "228":
                continue

            print(input_name)
            graph, num_buses, size_bus, constraints = parse_input(category_path + "/" + input_name)
            solution = solve(graph, num_buses, size_bus, constraints)
            output_file = open(output_category_path + "/" + input_name + ".out", "w")

            #TODO: modify this to write your solution to your 
            #      file properly as it might not be correct to 
            #      just write the variable solution to a file
            for i in solution:
                output_file.write(str(i) + "\n")

            output_file.close()

if __name__ == '__main__':
    main()


