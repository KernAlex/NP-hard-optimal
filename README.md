# NP-hard-optimal
# CS170– Fall 2018— Solver Design Doc

## Freddy Cervantes: SID 3033250924, Alex Kern: SID 27046342, Haitao Zhu: SID 3033251184

## December 2, 2018

## Stage 1: Rowdy Problem

The first step the algorithm does to solve the problem is take care of the rowdy kids. The
algorithm does this in a set cover fashion. So given a list of rowdy groups. The algorithm iterates
through the sets and finds student i with the most instances and sets him in the first bus. After,
the algorithm iterates through the sets and removes all the sets containing i student. Now on the
queue of sets to bee seen, we do not have any set with student i. We repeat the algorithm, finding
the next student with the most instances and setting that student with the first student. By the
end of this first stage, all the rowdiest students will be sat together in the first bus, or first set of
buses depending on the the size capacity of the bus.

## Stage 2: Optimizing Edges

Now that we have the rowdy children removed, the goal is optimizing the friend sets. Using
the software ”Mosek,” a quadratic optimization model was formed maximizing the edges for each
bus. Imagine a fully connected 3 vertices graph, such that we havevi∈v 1 , v 2 , v 3. We say an edge
exists in a subset ifvi∗vj== 1. this can only happen ifvi== 1∧vj== 1, else the edge will have
been ”removed”. In the case of a fully connected 3 vertices graph the edges are accounted for by
the equationN umEdges=v 1 ∗v 2 +v 1 ∗v 3 +v 2 ∗v 3. Note that in this case each vertices exists in
the graph. Say we wanted to remove one of the edges,v 2 such thatv 1 == 1∧v 2 == 0∧v 3 == 1.
Then it is the case that NumEdges is equal to 1, and we have filled a bus of size 2. We use the
edge-incident matrix H to accomplish this, by the following quadratic maximization equation:

```
