from AlgoritmoExatoIsoAED import GrafoIsomorfo
from matplotlib import pyplot as plt

import networkx as nx

if __name__ == "__main__":

    teste = GrafoIsomorfo()

    G = nx.Graph()

    G.add_nodes_from([1, 2, 3, 4, 5])
    G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])

    nx.draw(G, with_labels=True)

    plt.show()

    H = nx.Graph()
    H.add_nodes_from(['a', 'b', 'c', 'd', 'e'])
    H.add_edges_from([('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'a')])
    nx.draw(H, with_labels=True)

    plt.show()

    M = teste.contrairGrafos(H, ('b', 'c'))
    nx.draw(M, with_labels=True)

    plt.show()

    print(teste.isIsomorfos(H, M))  # False

    """
    G1 = nx.Graph()

    G1.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9])
    G1.add_edges_from([(1, 3), (2, 3), (3, 4), (3, 6), (5, 6), (6, 7), (7, 8), (6, 9), (9, 10)])

    nx.draw(G1, with_labels=True)

    plt.show()

    M = teste.contrairGrafos(G1, (2, 3))
    nx.draw(M, with_labels=True)

    plt.show()

    print(teste.isIsomorfos(G1, M))  # False
    
    G = nx.Graph()

    G.add_nodes_from([1, 2, 3, 4, 5])
    G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])

    nx.draw(G, with_labels=True)

    plt.show()

    H = nx.Graph()
    H.add_nodes_from(['a', 'b', 'c', 'd', 'e'])
    H.add_edges_from([('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'a')])
    nx.draw(H, with_labels=True)

    plt.show()

    M = teste.contrairGrafos(H, ('b', 'c'))
    nx.draw(M, with_labels=True)

    plt.show()

    print(teste.isIsomorfos(H, M))  # False


    A = nx.Graph()
    A.add_nodes_from([1, 2, 3, 4, 5])
    A.add_edges_from([(1, 4), (1, 2), (1, 5), (2, 5), (2, 3), (3, 4), (3, 5)])
    nx.draw(A)

    B = nx.Graph()
    B.add_nodes_from(['a', 'b', 'c', 'd', 'e'])
    B.add_edges_from([('a', 'b'), ('a', 'c'), ('a', 'e'), ('c', 'd'), ('d', 'e'), ('b', 'd'), ('c', 'e')])
    nx.draw(B)

    print(teste.isIsomorfos(A, B))  # True
    """

   # C = nx.Graph([(1, 3), (2, 3), (3, 4), (3, 6), (5, 6), (6, 7), (7, 8), (6, 9), (9, 10)])
   # nx.draw(C)

    # D = nx.Graph(
    #    [('a', 'c'), ('b', 'c'), ('c', 'd'), ('c', 'e'), ('e', 'f'), ('f', 'h'), ('g', 'h'), ('h', 'j'), ('h', 'i')])
    #nx.draw(D)

    #nx.isomorphism

    #print(teste.isIsomorfos(C, D))  # False
"""
    E = nx.Graph([(1, 2), (2, 3), (1, 5), (5, 3), (4, 5), (4, 3), (1, 4)])
    #E = nx.Graph([(1, 2), (2, 3), (4, 3), (1, 4)])
    nx.draw(E)

    F = nx.Graph([('a', 'e'), ('a', 'b'), ('b', 'e'), ('d', 'e'), ('c', 'd'), ('b', 'd'), ('b', 'c')])
    nx.draw(F)

    print(teste.isIsomorfos(E, F))  # False

    I = nx.Graph([(1, 5), (1, 2), (2, 6), (3, 6), (3, 4), (5, 6), (4, 5), (1, 4), (2, 3)])
    nx.draw(I)

    J = nx.Graph(
        [('a', 'b'), ('a', 'e'), ('e', 'f'), ('b', 'f'), ('a', 'c'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('d', 'f')])
    nx.draw(J)

    print(teste.isIsomorfos(I, J))  # True

    K = nx.Graph([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (1, 8), (1, 5), (2, 8), (3, 7), (4, 6)])
    nx.draw(K)

    L = nx.Graph(
        [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'f'), ('f', 'g'), ('g', 'h'), ('a', 'h'), ('a', 'f'),
         ('b', 'e'), ('c', 'h'), ('d', 'g')])
    nx.draw(L)

    print(teste.isIsomorfos(K, L))  # False

    M = nx.Graph([(1, 2), (2, 3), (3, 4), (1, 4), (5, 6), (6, 7), (7, 8), (5, 8), (4, 8), (3, 7)])
    nx.draw(M)

    N = nx.Graph([(1, 2), (2, 4), (3, 4), (1, 3), (5, 6), (6, 8), (7, 8), (5, 7), (3, 5), (2, 8)])
    nx.draw(N)

    print(teste.isIsomorfos(M, N))  # False
"""