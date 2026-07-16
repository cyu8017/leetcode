class Solution:
    def createTargetArray(self, nums, index):
        out=[]
        for x,i in zip(nums,index):out.insert(i,x)
        return out
