class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        if len(connections) < n - 1:
            return -1  

        
        graph = {i: [] for i in range(n)}
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        components = 0

        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                components += 1

        
        return components - 1
