# LeetCode 3976 - Maximum Subarray Sum After Multiplier
# https://leetcode.com/problems/maximum-subarray-sum-after-multiplier/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_subarray_sum(nums, k)
  n = nums.length
  inf = -(2**53) / 4
  f = Array.new(n + 1) { Array.new(4, inf) }
  f[0][0] = 0
  ans = inf
  (1..n).each do |i|
    x = nums[i - 1]
    f[i][0] = [f[i - 1][0], 0].max + x
    f[i][1] = [[f[i - 1][0], f[i - 1][1]].max, 0].max + x * k
    f[i][2] = [[f[i - 1][0], f[i - 1][2]].max, 0].max + (x.to_f / k).to_i
    f[i][3] = [[f[i - 1][1], f[i - 1][2]].max, f[i - 1][3]].max + x
    v = [[f[i][0], f[i][1]].max, [f[i][2], f[i][3]].max].max
    ans = v if v > ans
  end
  ans
end
