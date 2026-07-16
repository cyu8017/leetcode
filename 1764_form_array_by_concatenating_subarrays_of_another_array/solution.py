class Solution:
    def canChoose(self, groups, nums):
        n = len(nums)
        def dfs(i, start):
            if i == len(groups):
                return start == n
            g = groups[i]
            m = len(g)
            for j in range(start, n - m + 1):
                if nums[j:j + m] == g and dfs(i + 1, j + m):
                    return True
            return False
        return dfs(0, 0)
