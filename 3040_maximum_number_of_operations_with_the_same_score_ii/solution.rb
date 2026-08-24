# LeetCode 3040 - Maximum Number of Operations With the Same Score II
# https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/

# @param {Integer[]} nums
# @return {Integer}
def max_operations(nums)
  n = nums.length
  1 + [
    ops_g(nums, n, 2, n - 1, nums[0] + nums[1]),
    ops_g(nums, n, 0, n - 3, nums[n - 1] + nums[n - 2]),
    ops_g(nums, n, 1, n - 2, nums[0] + nums[n - 1])
  ].max
end

def ops_g(nums, n, i0, j0, score)
  f = Array.new(n) { Array.new(n, -1) }
  dfs = lambda do |i, j|
    return 0 if j - i < 1
    return f[i][j] if f[i][j] != -1

    ans = 0
    ans = [ans, 1 + dfs.call(i + 2, j)].max if nums[i] + nums[i + 1] == score
    ans = [ans, 1 + dfs.call(i + 1, j - 1)].max if nums[i] + nums[j] == score
    ans = [ans, 1 + dfs.call(i, j - 2)].max if nums[j - 1] + nums[j] == score
    f[i][j] = ans
    ans
  end
  dfs.call(i0, j0)
end
