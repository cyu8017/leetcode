# LeetCode 3117 - Minimum Sum of Values by Dividing Array
# https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array/

# @param {Integer[]} nums
# @param {Integer[]} and_values
# @return {Integer}
def minimum_value_sum(nums, and_values)
  inf = 1 << 29
  n = nums.length
  m = and_values.length
  f = {}

  dfs = lambda do |i, j, a|
    return inf if n - i < m - j
    return i == n ? 0 : inf if j == m
    a &= nums[i]
    return inf if a < and_values[j]
    key = [i, j, a]
    return f[key] if f.key?(key)
    ans = dfs.call(i + 1, j, a)
    ans = [ans, dfs.call(i + 1, j + 1, -1) + nums[i]].min if a == and_values[j]
    f[key] = ans
    ans
  end

  ans = dfs.call(0, 0, -1)
  ans < inf ? ans : -1
end
