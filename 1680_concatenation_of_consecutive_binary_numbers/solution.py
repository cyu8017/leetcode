class Solution:
    def concatenatedBinary(self, n):
        ans=bits=0;mod=1000000007
        for x in range(1,n+1):
            if x&(x-1)==0:bits+=1
            ans=((ans<<bits)+x)%mod
        return ans
