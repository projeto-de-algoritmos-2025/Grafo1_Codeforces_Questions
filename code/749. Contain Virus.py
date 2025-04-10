class Solution(object):
    def containVirus(self, isInfected):
        """
        :type isInfected: List[List[int]]
        :rtype: int
        """
        from collections import deque

        m, n = len(isInfected), len(isInfected[0])
        total_walls = 0
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        while True:
            visited = [[False]*n for _ in range(m)]
            regions = []
            frontiers = []
            walls_needed = []

            # 1. Encontrar todas as regiões infectadas ativas
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1 and not visited[i][j]:
                        region = []
                        frontier = set()
                        walls = 0
                        queue = deque()
                        queue.append((i, j))
                        visited[i][j] = True

                        while queue:
                            r, c = queue.popleft()
                            region.append((r, c))
                            for dr, dc in directions:
                                nr, nc = r + dr, c + dc
                                if 0 <= nr < m and 0 <= nc < n:
                                    if isInfected[nr][nc] == 0:
                                        frontier.add((nr, nc))
                                        walls += 1
                                    elif isInfected[nr][nc] == 1 and not visited[nr][nc]:
                                        visited[nr][nc] = True
                                        queue.append((nr, nc))

                        regions.append(region)
                        frontiers.append(frontier)
                        walls_needed.append(walls)

            if not regions:
                break

            # 2. Escolher a região mais perigosa (que ameaça mais células não infectadas)
            max_index = 0
            for i in range(1, len(frontiers)):
                if len(frontiers[i]) > len(frontiers[max_index]):
                    max_index = i

            # 3. Adicionar muros na região escolhida
            total_walls += walls_needed[max_index]

            # 4. Conter a região escolhida (marcar como -1)
            for r, c in regions[max_index]:
                isInfected[r][c] = -1

            # 5. Outras regiões se espalham
            for i in range(len(regions)):
                if i == max_index:
                    continue
                for r, c in frontiers[i]:
                    isInfected[r][c] = 1

        return total_walls