class Solution:
    def kthSmallestPath(self, destination, k):
        import math
        v,h=destination; ans=[]
        while h+v:
            if h:
                count=math.comb(h+v-1,v)
                if k<=count: ans.append("H"); h-=1; continue
                k-=count
            ans.append("V"); v-=1
        return "".join(ans)
