"""
Instituto de Ciências Exatas
Departamento de Ciência da Computação
Pós-Graduação em Computação Aplicada

Disciplina:
Algorítmos e Estrutudas de Dados

Professor:
Edison Ishikawa

Alunos:
Eliane Cunha Marques
Hilario Luiz Babireski Junior
Joilton Almeida de Jesus
Leandro Willian Vasconcellos

Tema:

GT51: Graph Contractability

Pode um grafo isomorfo a H ser obtido de G por uma sequencia de contração de arestas?

"""

import networkx as nx
import numpy as np

from itertools import permutations


class GrafoIsomorfo:

    def isIsomorfos(self, G, H):
        """
        Verifica se dois grafos G e H são isomórficos.

        Esta função utiliza a técnica de força bruta para a verificação de isomorfismo
        e pode se tornar lenta de acordo com o tamanho do grafo (Quantidade de vértices
        e arestas)

        Parâmetros:
            G: Um grafo criado com a biblioteca networkx
            H: Um grafo criado com a biblioteca networkx

        Retorno:
            True se G e H forem isomorfos.
            False se G e H não forem isomorfos.

         """

        # Obtém a lista de vértices de cada grafo.
        n = len(G.nodes())
        m = len(H.nodes())

        """
        Verifica se os grafos contém o mesmo quantidade de vértices. Se a quantidade for diferente, já retorna
        False por não ser possível dois grafos com quantidades diferentes de vértices serem isomorfos. 
        """
        if n != m:
            return False
        else:
            """
            Caso contrário, é obtida a matriz de adjacências de G e as permutações de H de acordo com o número de 
            vértices de H.
            Faz-se a iteração na lista de permutações de H e dentro do laço obtem-se a matriz de adjacências de H
            de acordo com o índice da iteração.
            Em seguida faz-se a comparação direta da matriz de adjacências dos dois grafos, retornando True caso
            sejam consideradas iguais.
            """
            mat_adj_g = nx.adjacency_matrix(G)

            permutacoes_vertices = list(permutations(H.nodes(), m))

            for i in permutacoes_vertices:
                mat_adj_h = nx.adjacency_matrix(H, i)

                if np.all(mat_adj_h.toarray() == mat_adj_g.toarray()):
                    return True
            return False


    def contrairGrafos(self, g, v):
        """
        Contrai um grafo de acordo com uma lista (tupla) de vertices a serem contraídos.

        Parâmetros:
            g: Um grafo criado com a biblioteca networkx a ser contraído.
            v: Uma lista (tupla) de vertices a serem contraídos.

        Retorno:
            Um novo grafo criado com a exclusão dos vértices informados por parâmetro.
        """
        M = nx.contracted_edge(g, (v[0], v[1]), self_loops = False)

        return M

