class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import defaultdict

        # Criar o grafo como lista de adjacência
        grafo = defaultdict(list)
        for a, b in connections:
            grafo[a].append(b)
            grafo[b].append(a)

        # Arrays para armazenar o tempo de descoberta e o menor tempo alcançável
        discovery = [-1] * n
        low = [-1] * n
        tempo = [0]  # contador de tempo global
        resultado = []

        def dfs(no, pai):
            discovery[no] = low[no] = tempo[0]
            tempo[0] += 1

            for vizinho in grafo[no]:
                if vizinho == pai:
                    continue  # Não voltar para o pai
                if discovery[vizinho] == -1:
                    dfs(vizinho, no)
                    low[no] = min(low[no], low[vizinho])

                    # Verifica se a conexão é crítica
                    if low[vizinho] > discovery[no]:
                        resultado.append([no, vizinho])
                else:
                    # Atualiza o low se encontrar uma aresta de retorno
                    low[no] = min(low[no], discovery[vizinho])

        # Começar o DFS a partir do nó 0 (poderia ser qualquer nó)
        dfs(0, -1)

        return resultado
