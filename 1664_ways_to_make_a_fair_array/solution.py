class Solution:
    def waysToMakeFair(self, nums):
        te=sum(nums[::2]);to=sum(nums[1::2]);le=lo=ans=0
        for i,x in enumerate(nums):
            if i%2:to-=x
            else:te-=x
            if le+to==lo+te:ans+=1
            if i%2:lo+=x
            else:le+=x
        return ans
