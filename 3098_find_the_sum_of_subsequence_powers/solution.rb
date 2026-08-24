# LeetCode 3098 - Find the Sum of Subsequence Powers
# https://leetcode.com/problems/find-the-sum-of-subsequence-powers/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def sum_of_powers(nums, k)
  mod = 1_000_000_007
  nums = nums.sort
  n = nums.length
  f = {}

  dfs = lambda do |i, j, kk, mi|
    return mi if i >= n && kk == 0
    return 0 if i >= n
    return 0 if n - i < kk
    key = [mi, i, j, kk]
    return f[key] if f.key?(key)
    ans = dfs.call(i + 1, j, kk, mi)
    if j == n
      ans = (ans + dfs.call(i + 1, i, kk - 1, mi)) % mod
    else
      ans = (ans + dfs.call(i + 1, i, kk - 1, [mi, nums[i] - nums[j]].min)) % mod
    end
    f[key] = ans
    ans
  end

  dfs.call(0, n, k, 10**18)
end
