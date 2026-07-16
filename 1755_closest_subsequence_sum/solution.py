class Solution:
    def minAbsDifference(self, nums, goal):
        n = len(nums)
        left = nums[:n // 2]
        right = nums[n // 2:]
        def sums(arr):
            vals = [0]
            for x in arr:
                vals += [v + x for v in vals]
            return sorted(vals)
        a, b = sums(left), sums(right)
        best = float("inf")
        j = len(b) - 1
        for x in a:
            while j and abs(x + b[j] - goal) >= abs(x + b[j - 1] - goal):
                j -= 1
            best = min(best, abs(x + b[j] - goal))
        return best
