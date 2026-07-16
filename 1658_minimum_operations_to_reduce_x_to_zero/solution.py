class Solution:
    def minOperations(self, nums, x):
        target=sum(nums)-x
        if target<0:return -1
        best=-1; left=cur=0
        for right,v in enumerate(nums):
            cur+=v
            while cur>target:cur-=nums[left];left+=1
            if cur==target:best=max(best,right-left+1)
        return -1 if best<0 else len(nums)-best
