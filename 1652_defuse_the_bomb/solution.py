class Solution:
    def decrypt(self, code, k):
        n=len(code)
        if k==0:return [0]*n
        a=code*2; ans=[]
        for i in range(n):
            ans.append(sum(a[i+1:i+k+1]) if k>0 else sum(a[i+n+k:i+n]))
        return ans
