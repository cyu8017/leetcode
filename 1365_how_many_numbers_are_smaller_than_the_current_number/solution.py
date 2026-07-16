class Solution:
    def smallerNumbersThanCurrent(self, nums):
        rank={x:i for i,x in enumerate(sorted(nums)) if x not in locals().get('rank',{})}
        return [sorted(nums).index(x) for x in nums]
