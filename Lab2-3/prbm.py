graph = {
}
visited = []  # List to keep track of visited nodes.
queue = []  # Initialize a queue


def isValid(node):
    left_side = node[:1]  # Ramanem cu malul stang din instanta
    right_side = node[2:3]  # Ramanem cu malul drept din instanta
    left_vector = []  # Transformam elementul din lista in vector
    for i in left_side:
        left_vector = i
    '''
    Pt fiecare nevasta care se afla pe pozitie impara, verificam sotul ei
    este alaturi. Daca nu e, verificam daca exista alti soti pe mal. Altfel e valid.
    '''
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


def is_final(node, final_node):
    if node == final_node:
        return True
    return False


def new_node(node, x, y):
    left_side = node[:1]  # Ramanem cu malul stang din instanta
    right_side = node[2:3]  # Ramanem cu malul drept din instanta
    left_vector = []  # Transformam elementul din lista in vector
    left_vector = list(left_side)
    left_vector = list(left_vector[0])

    right_vector = list(right_side)
    right_vector = list(right_vector[0])

    for i in node[1:2]:
        direction = i
    aux = left_vector[x]
    left_vector[x] = right_vector[x]
    right_vector[x] = aux

    if y != -1:
        aux2 = left_vector[y]
        left_vector[y] = right_vector[y]
        right_vector[y] = aux2

    changed_node = (left_vector, direction, right_vector)
    return changed_node


'''def new_node1(node, x):
    left_side = node[:1]  # Ramanem cu malul stang din instanta
    right_side = node[2:3]  # Ramanem cu malul drept din instanta
    left_vector = []  # Transformam elementul din lista in vector
    left_vector = list(left_side)
    left_vector = list(left_vector[0])

    right_vector = list(right_side)
    right_vector = list(right_vector[0])

    for i in node[1:2]:
        direction = i
    aux = left_vector[x]
    left_vector[x] = right_vector[x]
    right_vector[x] = aux

    changed_node = (left_vector, direction, right_vector)
    return changed_node'''


# functia de mai jos genereaza toate tranzitiile posibile
def choose_persons_to_move_on_bfs(node):
    left_side = node[:1]  # Ramanem cu malul stang din instanta
    print('Hello left side: ', left_side)
    right_side = node[2:3]  # Ramanem cu malul drept din instanta

    left_vector = list(left_side)
    left_vector = list(left_vector[0])
    print('Left vector: ', left_vector)
    # print('Left vector element: ', left_vector[0])
    # left_vector.append(2)
    # print('Left vector after append: ', left_vector)
    # print('Left side after append: ', left_side[0])

    right_vector = list(right_side)
    right_vector = list(right_vector[0])
    '''print('Right vector: ', right_vector)
    print('Right vector element: ', right_vector[0])
    right_vector.append(2)
    print('Right vector after append: ', right_vector)
    print('Right side after append: ', right_side[0])
    '''
    # if node[1:2]==False:
    # Mergem cu dreapta
    # luam cate 2 persoane
    k = 0
    list_of_new_nodes = []
    while k < len(left_vector):
        j = k + 1
        while j < len(left_vector) - 1:
            if left_vector[k] == 1 and left_vector[j] == 1:
                aux = list(new_node(node, k, j))
                if isValid(aux):
                    list_of_new_nodes.append(aux)  # Lista tuturor posibilitatilor valide din starea curenta
            j += 1
        k += 1
    # luam cate o persoana
    k = 0
    while k < len(left_vector):
        if left_vector[k] == 1:
            aux = list(new_node(node, k, -1))
            if isValid(aux):
                list_of_new_nodes.append(aux)  # Lista tuturor posibilitatilor valide din starea curenta
        k += 1
    return list_of_new_nodes


'''def generateGraf(node):
    graph = {
        node: choose_persons_to_move_on_bfs(node)

    }
    return graph
'''

def choose_persons_to_move_on_back(node):
    left_side = node[:1]  # Ramanem cu malul stang din instanta
    right_side = node[2:3]  # Ramanem cu malul drept din instanta
    left_vector = []  # Transformam elementul din lista in vector
    for i in left_side:
        left_vector = i
    right_vector = []
    for i in right_side:
        right_vector = i
    # if node[1:2]==False:
    # Mergem cu dreapta
    k = 0
    listOfNewNodes = []
    while k < len(left_vector):
        j = k + 1
        while j < len(left_vector) - 1:
            if left_vector[k] == 1 and left_vector[j] == 1:
                listOfNewNodes.append(new_node(node, k, j))  # Lista tuturor posibilitatilor valide din starea curenta
            j += 1
        k += 1
    return listOfNewNodes


def add_to_graph(graph, el, list_of_new_nodes):
    graph.append(el, list_of_new_nodes)


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


def parcurgereBFS(node, final_node):
    if is_final(node, final_node):
        bfs(visited, graph, initialState)
    list_of_new_nodes = choose_persons_to_move_on_bfs(node)
    add_to_graph(graph, node, list_of_new_nodes)
    for el in list_of_new_nodes:
        parcurgere(el, final_node)


def parcurgere(el, finalNode):
    pass


def parcurgereBack(node, finalNode):
    if is_final(node, finalNode):
        bfs(visited, graph, initialState)
    list_of_new_nodes = choose_persons_to_move_on_back(node)
    add_to_graph(graph, node, list_of_new_nodes)
    for el in list_of_new_nodes:
        parcurgere(el, finalNode)


def parcurgereHill(node, final_node):
    pass


def parcurgereA(node, final_node):
    pass


'''def menu():
    n = int(input("Numarul de cupluri este:"))
    n = n * 2
    right_side = [0] * n
    left_side = [1] * n
    way_of_boat = True
    node = (left_side, way_of_boat, right_side)
    final_node = (right_side, not way_of_boat, left_side)
    print("State-ul initial este: ", node)
    print("State-ul final este: ", final_node)
    print("Selecteaza metoda prin care doresti sa rezolvi problema:")
    print("1. Backtracking")
    print("2. BFS")
    print("3. HillClimbing")
    print("4. A*")
    k = int(input("Varianta aleasa: "))
    if k == 1:
        parcurgereBack(node, final_node)
    if k == 2:
        parcurgereBFS(node, final_node)
    if k == 3:
        parcurgereHill(node, final_node)
    if k == 4:
        parcurgereA(node, final_node)

'''


def init(n):
    n = n * 2
    right_side = [0] * n
    left_side = [1] * n
    way_of_boat = True
    node = (left_side, way_of_boat, right_side)
    print(choose_persons_to_move_on_bfs(node))


# node2 = ([1, 1, 1, 1], True, [0, 0, 0, 0])
# isValid functioneaza
# print(isValid(node2))
# testam tranzitiile
# print(choose_persons_to_move_on_bfs(node2))
# menu()
n = int(input("Numarul de cupluri este:"))
init(n)
#print(generateGraf(n))
