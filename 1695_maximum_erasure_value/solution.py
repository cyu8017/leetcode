class Solution:
    def maximumUniqueSubarray(self, nums):
        seen={};left=cur=best=0
        for right,x in enumerate(nums):
            if x in seen and seen[x]>=left:
                stop=seen[x]
                while left<=stop:cur-=nums[left];left+=1
            seen[x]=right;cur+=x;best=max(best,cur)
        return best
