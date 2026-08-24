# LeetCode 3196 - Maximize Total Cost of Alternating Subarrays
# https://leetcode.com/problems/maximize-total-cost-of-alternating-subarrays/

# @param {Integer[]} nums
# @return {Integer}
def maximum_total_cost(nums)
  neg = -10**18
  n = nums.length
  memo = Array.new(n) { [neg, neg] }
  dfs = lambda do |i, j|
    return 0 if i >= n
    return memo[i][j] if memo[i][j] != neg
    res = nums[i] + dfs.call(i + 1, 1)
    res = [res, -nums[i] + dfs.call(i + 1, 0)].max if j > 0
    memo[i][j] = res
  end
  dfs.call(0, 0)
end
