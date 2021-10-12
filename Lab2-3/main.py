from copy import deepcopy

'''
def is_valid(node):
    left_side = node[:1]  # Ramanem cu malul stang din instanta
    right_side = node[2:3]  # Ramanem cu malul drept din instanta
    left_vector = []  # Transformam elementul din lista in vector
    for i in left_side:
        left_vector = i
    
    #Pt fiecare nevasta care se afla pe pozitie impara, verificam sotul ei
    #este alaturi. Daca nu e, verificam daca exista alti soti pe mal. Altfel e valid.
    
    right_vector = []
    for i in right_side:
        right_vector = i
    valid = True
    k = 1
    k2 = 0
    husbands_found = 0
    while k2 < len(left_vector):
        if left_vector[k2] == 1:
            husbands_found += 1
        k2 += 2

    while k < len(left_vector):
        if left_vector[k] == 1:
            if left_vector[k - 1] == 1:
                valid = True
            elif husbands_found == 0:
                valid = True
            else:
                valid = False
        if not valid:
            return False
        k += 2
    k = 1
    k2 = 0
    husbands_found = 0
    while k2 < len(right_vector):
        if right_vector[k2] == 1:
            husbands_found += 1
        k2 += 2
    while k < len(right_vector):
        if right_vector[k] == 1:
            if right_vector[k - 1] == 1:
                valid = True
            elif husbands_found == 0:
                valid = True
            else:
                valid = False
        if not valid:
            return False
        k += 2
    return True

'''


def is_final(node, finalNode):
    if node == finalNode:
        return True
    return False


def new_node(node, x, y):
    left_side = node[:1]  # Ramanem cu malul stang din instanta
    right_side = node[2:3]  # Ramanem cu malul drept din instanta
    left_vector = []  # Transformam elementul din lista in vector
    for i in left_side:
        left_vector = i
    right_vector = []
    for i in right_side:
        right_vector = i
    for i in node[1:2]:
        direction = i
    aux = left_vector[x]
    left_vector[x] = right_vector[x]
    right_vector[x] = aux
    aux2 = left_vector[y]
    left_vector[y] = right_vector[y]
    right_vector[y] = aux2

    changed_node = (left_vector, direction, right_vector)
    return changed_node


def choosePersonsToMove(node):
    leftSide = node[:1]  # Ramanem cu malul stang din instanta
    rightSide = node[2:3]  # Ramanem cu malul drept din instanta
    leftVector = []  # Transformam elementul din lista in vector
    for i in leftSide:
        leftVector = i
    rightVector = []
    for i in rightSide:
        rightVector = i
    # if node[1:2]==False:
    # Mergem cu dreapta
    k = 0
    while k < len(leftVector):
        j = k + 1
        while j < len(leftVector) - 1:
            if leftVector[k] == 1 and leftVector[j] == 1:
                print(newNode(node, i, j))


n = int(input("Numarul de cupluri este:"))
n = n * 2

rightSide = [0] * n
leftSide = [1] * n
# Sotii se afla pe pozitiile pare iar sotiile pe pozitiile impare( ex: v[2] este sot)
# Perechile intre sot sotie se determina prin (k,k-1), k>1. Ex: v[2] si v[3] sunt cuplu iar v[2] si v[1] nu sunt.
# Malul stang contine la inceput doar valori de 1 pentru ca toate cuplurile sunt in el
# Malul drept contine la inceput doar valori de 0 pentru ca inca nu s-a facut nicio mutare

wayOfBoat = True
# TRUE inseamna ca directia barcii va fi spre dreapta
# FALSE inseamna ca directia barcii va fi spre stanga

node = (leftSide, wayOfBoat, rightSide)

# Starea initiala( toate cuplurile sunt pe malul stang)
initialState = node

# Starea finala ( toate cuplurile sunt pe malul drept)
finalState = (rightSide, False, leftSide)

# print("De aici incepe distractia")
# choosePersonsToMove(initialState)
print("Starea initiala:", initialState)
print("Starea finala:", finalState)


'''
node2 = ([1, 0, 1, 1, 0, 1], True, [0, 1, 0, 0, 1, 0])

print(finalState)

print(new_node(finalState, 2, 4))

print(is_final(node2, finalState))

print(is_valid(node2))

tup = (1, 2, [])
put = deepcopy(tup)
tup[2].append('hello')
print(tup)
l = list(put) #copiaza o tupla 
l.append(3)
print(tuple(l))
print(put)
'''

# mixed list
prime_numbers = [2, 3, 5]

# copying a list
numbers = prime_numbers.copy()

numbers.append(4);
print('Prime List:', prime_numbers)

print('Copied List:', numbers)

# Output: Copied List: [2, 3, 5]

import networkx as nx
G = nx.Graph()
H = nx.Graph()
G.add_node(1)
G.add_nodes_from([2, 3])
G.add_nodes_from(range(4, 7))
H.add_node(7)
G.add_nodes_from(H)
G.add_edge(1, 2)
G.add_edge(1, 1)
G.add_edges_from([(2,3), (3,6), (4,6), (5,6)])
H.add_edges_from([(4,7), (5,7), (6,7)])
G.add_edges_from(H.edges())
nx.draw_networkx(G)
