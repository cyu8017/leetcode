# LeetCode 3077 - Maximum Strength of K Disjoint Subarrays
# https://leetcode.com/problems/maximum-strength-of-k-disjoint-subarrays/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximum_strength(nums, k)
  n = nums.length
  inf = -(1 << 53) / 2
  f = Array.new(n + 1) { Array.new(k + 1) { [inf, inf] } }
  f[0][0][0] = 0
  (1..n).each do |i|
    x = nums[i - 1]
    (0..k).each do |j|
      sign = (j & 1) != 0 ? 1 : -1
      val = sign * x * (k - j + 1)
      f[i][j][0] = [f[i - 1][j][0], f[i - 1][j][1]].max
      f[i][j][1] = [f[i][j][1], f[i - 1][j][1] + val].max
      if j > 0
        t = [f[i - 1][j - 1][0], f[i - 1][j - 1][1]].max + val
        f[i][j][1] = [f[i][j][1], t].max
      end
    end
  end
  [f[n][k][0], f[n][k][1]].max
end
