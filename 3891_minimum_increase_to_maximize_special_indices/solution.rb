# LeetCode 3891 - Minimum Increase to Maximize Special Indices
# https://leetcode.com/problems/minimum-increase-to-maximize-special-indices/

# @param {Integer[]} nums
# @return {Integer}
def min_increase(nums)
  n = nums.length
  f = Array.new(n) { [-1, -1] }
  dfs = nil
  dfs = lambda do |i, j|
    return 0 if i >= n - 1
    return f[i][j] if f[i][j] != -1
    cost = [0, [nums[i - 1], nums[i + 1]].max + 1 - nums[i]].max
    ans = cost + dfs.call(i + 2, j)
    ans = [ans, dfs.call(i + 1, 0)].min if j > 0
    f[i][j] = ans
    ans
  end
  dfs.call(1, (n & 1) ^ 1)
end
