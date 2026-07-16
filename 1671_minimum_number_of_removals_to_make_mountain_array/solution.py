class Solution:
    def minimumMountainRemovals(self, nums):
        from bisect import bisect_left
        def lis(a):
            d=[];out=[]
            for x in a:
                i=bisect_left(d,x)
                if i==len(d):d.append(x)
                else:d[i]=x
                out.append(i+1)
            return out
        l=lis(nums);r=lis(nums[::-1])[::-1];n=len(nums)
        return n-max((l[i]+r[i]-1 for i in range(n) if l[i]>1 and r[i]>1),default=0)
