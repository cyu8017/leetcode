class Solution:
    def getSumAbsoluteDifferences(self, nums):
        total=sum(nums);left=0;n=len(nums);ans=[]
        for i,x in enumerate(nums):
            ans.append(x*i-left+(total-left-x)-x*(n-i-1));left+=x
        return ans
