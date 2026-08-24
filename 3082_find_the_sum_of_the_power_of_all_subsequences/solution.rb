# LeetCode 3082 - Find the Sum of the Power of All Subsequences
# https://leetcode.com/problems/find-the-sum-of-the-power-of-all-subsequences/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def sum_of_power(nums, k)
  mod = 1_000_000_007
  n = nums.length
  f = Array.new(n + 1) { Array.new(k + 1, 0) }
  f[0][0] = 1
  (1..n).each do |i|
    (0..k).each do |j|
      f[i][j] = (f[i - 1][j] * 2) % mod
      f[i][j] = (f[i][j] + f[i - 1][j - nums[i - 1]]) % mod if j >= nums[i - 1]
    end
  end
  f[n][k]
end
