class Solution:
    def hasValidPath(self, grid):
        dirs={1:((0,-1),(0,1)),2:((-1,0),(1,0)),3:((0,-1),(1,0)),4:((0,1),(1,0)),5:((0,-1),(-1,0)),6:((0,1),(-1,0))}
        m,n=len(grid),len(grid[0]);seen={(0,0)};st=[(0,0)]
        while st:
            r,c=st.pop()
            if (r,c)==(m-1,n-1):return True
            for dr,dc in dirs[grid[r][c]]:
                x,y=r+dr,c+dc
                if 0<=x<m and 0<=y<n and (x,y) not in seen and (-dr,-dc) in dirs[grid[x][y]]:
                    seen.add((x,y));st.append((x,y))
        return False
