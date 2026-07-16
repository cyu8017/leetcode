class Solution:
    def createSortedArray(self, instructions):
        MOD=1000000007; size=max(instructions,default=0)+2; bit=[0]*(size+1)
        def query(i):
            s=0
            while i: s+=bit[i]; i-=i&-i
            return s
        ans=0
        for i,x in enumerate(instructions):
            ans=(ans+min(query(x-1),i-query(x)))%MOD
            j=x
            while j<=size: bit[j]+=1; j+=j&-j
        return ans
