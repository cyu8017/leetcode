from collections import deque
class Solution:
    def minCost(self, grid):
        m,n=len(grid),len(grid[0]); dist=[[10**9]*n for _ in range(m)]; dist[0][0]=0
        q=deque([(0,0)]); dirs=((0,1),(0,-1),(1,0),(-1,0))
        while q:
            r,c=q.popleft()
            for k,(dr,dc) in enumerate(dirs,1):
                x,y=r+dr,c+dc
                if 0<=x<m and 0<=y<n:
                    w=k!=grid[r][c]; nd=dist[r][c]+w
                    if nd<dist[x][y]:
                        dist[x][y]=nd
                        (q.append if w else q.appendleft)((x,y))
        return dist[-1][-1]
