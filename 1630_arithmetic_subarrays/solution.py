class Solution:
    def checkArithmeticSubarrays(self, nums, l, r):
        ans = []
        for a, b in zip(l, r):
            x = sorted(nums[a:b+1]); ans.append(len(x) < 3 or len(set(x[i+1]-x[i] for i in range(len(x)-1))) == 1)
        return ans
