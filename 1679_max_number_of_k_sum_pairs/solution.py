class Solution:
    def maxOperations(self, nums, k):
        from collections import Counter
        c=Counter();ans=0
        for x in nums:
            if c[k-x]:c[k-x]-=1;ans+=1
            else:c[x]+=1
        return ans
