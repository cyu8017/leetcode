class Solution:
    def getMaxGridHappiness(self, m, n, introvertsCount, extrovertsCount):
        from functools import lru_cache
        states=3**n
        cells=[]; intro=[]; extro=[]; row=[]
        for s in range(states):
            x=s; a=[]
            for _ in range(n):a.append(x%3);x//=3
            cells.append(a); intro.append(a.count(1)); extro.append(a.count(2))
            val=sum(120 if z==1 else 40 if z==2 else 0 for z in a)
            for j in range(1,n):
                val += self._pair(a[j-1],a[j])
            row.append(val)
        compat=[[sum(self._pair(cells[a][j],cells[b][j]) for j in range(n)) for b in range(states)] for a in range(states)]
        @lru_cache(None)
        def dp(r,prev,i,e):
            if r==m:return 0
            return max(row[s]+compat[prev][s]+dp(r+1,s,i-intro[s],e-extro[s])
                       for s in range(states) if intro[s]<=i and extro[s]<=e)
        return dp(0,0,introvertsCount,extrovertsCount)
    def _pair(self,a,b):
        if not a or not b:return 0
        return (-30 if a==1 else 20)+(-30 if b==1 else 20)
