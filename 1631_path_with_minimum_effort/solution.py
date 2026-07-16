class Solution:
    def minimumEffortPath(self, heights):
        import heapq
        m, n = len(heights), len(heights[0]); dist = [[float("inf")]*n for _ in range(m)]
        dist[0][0] = 0; heap = [(0,0,0)]
        while heap:
            effort, i, j = heapq.heappop(heap)
            if (i,j) == (m-1,n-1): return effort
            if effort != dist[i][j]: continue
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                x,y=i+di,j+dj
                if 0<=x<m and 0<=y<n:
                    nd=max(effort,abs(heights[i][j]-heights[x][y]))
                    if nd<dist[x][y]: dist[x][y]=nd; heapq.heappush(heap,(nd,x,y))
