__________________________________________________
********** CS170 Fall 2018 Project **********
__________________________________________________

    This project was created to solve an NP-Hard problem given to students of UC Berkeley's cs170
fall 2018 class. This project was given to test students of the material learned thorught the semester and to push them to deepen their understanding of material. The solutions given in this project are not to shared with other students. The problem to be solved is as follows:

    You are a tired, overworked teacher who has spent the last week organiz- ing a field trip for your entire middle school. The night before the trip, you realize you forgot to plan the most important part – transportation! Fortu- nately, your school has access to a large fleet of buses. Being the caring teacher you are, you’d like to ensure that students can still end up on the same bus as their friends. After some investigative work on social media, you’ve man- aged to figure out exactly who is friends with who at your school and begin to assign students to buses with the intent of breaking up as few friendships as possible. You’ve only just begun when you receive a frantic email from one of the chaperones for the trip. The kids this year are particularly rowdy, and the chaperones have given you a list of groups of students who get too rowdy when they are all together. If any of these groups are seated assigned to the same bus, they will all have to be removed from the bus and sent home. Can you plan transportation while keeping both the students and the chaperones happy?

    Formally, you’re given an undirected graph G = (V,E), an integer k, and an integer s, where each node in the graph denotes a student, and each edge (v1,v2) denotes that students v1 and v2 are friends. The integer k denotes the number of buses available and the integer s denotes the number of students that can fit on a single bus. Furthermore, you’re given a list L, where each element Lj is some subset of V which corresponds to a group that should be kept apart. You must return a partition of G – a set of sets of vertices Vi such that V1 ∪ V2 ∪ V3,∪...∪ Vk = V and ∀i not equal to j,Vi ∩ Vj = ∅. Additionally,∀i, 0 < |Vi| ≤ s. In other words, every bus must be non-empty, and must not have more students on it than its capacity allows. 

    Consider a vertex v to be valid if there is no i and j such that v ∈ Lj and Lj ⊂ Vi. In other words, a vertex is valid if it is not in a rowdy group whose members all end up on the same bus. For example, if one of the rowdy groups was ‘Alice’, ‘Bob’, and ‘Carol’, then putting ‘Alice’, ‘Bob’, ‘Carol’, and ’Dan’ on the same bus would lead to ‘Alice’, ‘Bob’, and ‘Carol’ being considered invalid vertices. However, a bus with just ‘Alice’, ‘Bob’, and ‘Dan’ would have no invalid vertices. 

    We’d like you to produce a partition that maximizes the percent of edges that occur between valid vertices in the same partition in the graph. The score for your partition is the percentage of edges (u, v) where u and v are both valid, and u, v ∈ Vi for some i. You’d like to produce a valid partition with as high a score as possible.

    *** Input ***: Each input consists of two files inside of a folder, graph.gml and parame- ters.txt. The first file will contain your graph G in the GML file format. Note that the labels of the vertices in your graph MUST be unique alphanumeric strings (this also means no whitespace). The second file is a text file and will start with two integers each on their own line; the first being k, the number of buses and the second being s, the number of students that fit on each bus. Every subsequent line will contain a non-empty list of vertices which compose a single “rowdy group” that should not all belong to the same bus. For a single input, the name of the folder that contains the above two files denotes the identifier of that input.

    Sample input parameters (Second File):
    3 # of number of buses
    5 # of students per bus
    [‘Harry’, ‘Hermione’, ‘Ron’]
    [‘Ron’, ‘Fred’, ‘George’]
    [‘Malfoy’, ‘Crabbe’, ‘Goyle’]

    *** Outout ***: For each input folder, you will generate a single output file with the name <input-identifer>.out (eg. if the folder was named “easy-input” then the output should be named “easy-input.out”). On each line of this file there will be a non empty list containing one of the subsets in your partition of the graph. Every node in the graph should appear exactly once in this file. The number of lines in this file should be exactly equal to the number of buses specified in the input file and no line should have more elements than the bus capacity specified in the input file.

    Sample output:
    [‘Harry’, ‘Hermione’, ‘George’]
    [‘Ron’, ‘Malfoy’, ‘Fred’]
    [‘Crabbe’, ‘Goyle’]


__________________________________________________
********** Getting Started **********
__________________________________________________

By following the following instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
Download the code from gradescope and open in prefered IDE or Terminal is desired.
__________________________________________________
********** Prerequisites **********
__________________________________________________

Mosek linear program optimizer for python is required. You will need a license to work with the library and install the
software based on computer specifications. For instruction and installing the software visit https://www.mosek.com/downloads/

In addition ensuring you will need to ensure you have NetworkX installed in your computer. For information on instructions and installing
visit https://networkx.github.io/documentation/stable/install.html

To test this project in your local machine you will require the following:
- Lastest updated version of Python
- Latest version of PIP if you are doing a PIP install
- Mosek installed with license

__________________________________________________
********** Installing **********
__________________________________________________

After meeting the required prerequisites you will need to set up your software environment if you wish to run the program on an IDE.
For this project pycharm and Spyder IDEs were used.

Spyder: If the prereqs were met, all that is required is that you run. No further action is needed do to anaconda already having all required
libraries installed.

Pycharm: Open the project on pycharm you will need to set up the environment. To do so, visit pycharm preferences. Ensure the interpreter is set
to your latest version of python. While in the same window, click on the plus symbol and install the mosek package. Now you are free to run
the algorithm with no problems.

__________________________________________________
********** Running the tests **********
__________________________________________________

To run tests simply run the doc tests.
__________________________________________________
********** Versioning **********
__________________________________________________

Version 1.1

__________________________________________________
********** Authors **********
__________________________________________________

Freddy Cervantes
Alex Kern
Haitao Zhu

See also the list of contributors who participated in this project.
__________________________________________________
********** Acknowledgments **********
__________________________________________________

Acknowledgement goes to the linear programing function provided by the mosek library. Also the functions of NetworkX which is the
primary graph library used in the creation of this project.