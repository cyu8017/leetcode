class Solution:
    def highestPeak(self, isWater):
        from collections import deque
        m, n = len(isWater), len(isWater[0])
        dist = [[-1] * n for _ in range(m)]
        q = deque()
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    dist[i][j] = 0
                    q.append((i, j))
        while q:
            i, j = q.popleft()
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and dist[x][y] == -1:
                    dist[x][y] = dist[i][j] + 1
                    q.append((x, y))
        return dist
