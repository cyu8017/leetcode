# LeetCode 3877 - Minimum Removals to Achieve Target XOR
# https://leetcode.com/problems/minimum-removals-to-achieve-target-xor/

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def min_removals(nums, target)
  mx = nums.max
  m = 0
  if mx > 0
    u = mx
    while u != 0
      m += 1
      u >>= 1
    end
  end
  return -1 if (1 << m) <= target
  n = nums.length
  nmask = 1 << m
  neg = -Float::INFINITY
  f = Array.new(n + 1) { Array.new(nmask, neg) }
  f[0][0] = 0
  (1..n).each do |i|
    x = nums[i - 1]
    nmask.times do |j|
      f[i][j] = f[i - 1][j]
      f[i][j] = [f[i][j], f[i - 1][j ^ x] + 1].max if f[i - 1][j ^ x] != neg
    end
  end
  return -1 if f[n][target] < 0
  n - f[n][target].to_i
end
