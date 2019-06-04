#from solver.py import parser_input

def rowdyKidSplitter(listOfRowdySets):
    """ This function gets the rowdiest kids and places them in the same bus.

    :param listOfRowdySets: This is a list containing all the lists of rowdy groups in the graph.
    :return: A bus with the rowdiest kids.

    >>> rowdyKidSplitter([[1,2,3], [2, 5, 6], [5, 3, 8]])
    [2, 5]
    >>> rowdyKidSplitter([[1, 2, 3], [2, 5, 6], [1, 7, 8], [3, 10, 9]])
    [2, 1, 3]
    >>> rowdyKidSplitter([[1,2, 3], [2, 4, 5], [7, 8, 9]])
    [2, 7]
    >>> rowdyKidSplitter([[1,5],[1,7],[1,9],[2,6],[2,8],[2,10],[6,7],[8,9],[4,16],[5,6,7,8,9,10],[3,11],[3,13],[3,15],[4,12],[4,14],[12,13],[14,15],[11,12,13,14,15,16],[23,31],[25,31],[27,31],[24,32],[26,32],[28,32],[24,25],[26,27],[17,29],[19,29],[17,18,19,20,21,22],[21,29],[18,30],[20,30],[22,30],[18,19],[20,21],[10,11],[16,17],[22,23],[28,29],[6,26],[8,25],[14,18],[13,21],[23,24,25,26,27,28]])
    [29, 6, 14, 25, 18, 13, 1, 32, 8, 3, 30, 31, 4, 27, 10, 20, 16, 22]
    >>> rowdyKidSplitter([[1,2,3,4],[1,5,6,7],[2,8,9,10],[2,11,12,13],[3,14,15,16],[3,18,19,20],[4,21,22,23],[4,24,25,26],[1,27,28,29]])
    [2, 3, 4, 1]

    """
    # The set that will contain the list of partition for the nodes.
    rowdyBus = []

    # Tracks the number of instances for the rowdy kids.
    instanceNumber = {}

    listOfRowdyGroups = listOfRowdySets[:]
    # Splits the group of spies into different buses.
    while listOfRowdyGroups:
        maxKid = [None, 0]
        for rowdySet in listOfRowdyGroups:
            for kid in rowdySet:
                if kid in instanceNumber:
                    instanceNumber[kid] = instanceNumber.get(kid) + 1
                else:
                    instanceNumber[kid] = 1
                if instanceNumber.get(kid) > maxKid[1]:
                    maxKid = [kid, instanceNumber.get(kid)]
        rowdyBus.append(maxKid[0])
        index = 0
        iterList = listOfRowdyGroups[:]
        for rowdySet in iterList:
            if maxKid[0] in rowdySet:
                listOfRowdyGroups.pop(index)
            else:
                index += 1

    return rowdyBus

