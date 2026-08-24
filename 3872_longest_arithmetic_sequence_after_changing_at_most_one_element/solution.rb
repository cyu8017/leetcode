# LeetCode 3872 - Longest Arithmetic Sequence After Changing At Most One Element
# https://leetcode.com/problems/longest-arithmetic-sequence-after-changing-at-most-one-element/

# @param {Integer[]} nums
# @return {Integer}
def longest_arithmetic(nums)
  n = nums.length
  d = Array.new(n, 0)
  (1...n).each { |i| d[i] = nums[i] - nums[i - 1] }
  f = Array.new(n, 2)
  g = Array.new(n, 2)
  f[0] = 1
  g[n - 1] = 1
  (2...n).each { |i| f[i] = f[i - 1] + 1 if d[i] == d[i - 1] }
  (n - 3).downto(0) { |i| g[i] = g[i + 1] + 1 if d[i + 1] == d[i + 2] }
  ans = 3
  n.times do |i|
    ans = [ans, [f[i], g[i]].max].max
    ans = [ans, f[i - 1] + 1].max if i > 0
    ans = [ans, g[i + 1] + 1].max if i + 1 < n
    if i > 0 && i < n - 1
      diff = nums[i + 1] - nums[i - 1]
      if diff.even?
        diff /= 2
        k = 3
        k += f[i - 1] - 1 if i > 1 && diff == d[i - 1]
        k += g[i + 1] - 1 if i < n - 2 && diff == d[i + 2]
        ans = [ans, k].max
      end
    end
  end
  ans
end
