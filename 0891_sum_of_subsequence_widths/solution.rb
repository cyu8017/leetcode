# LeetCode 0891 - Sum of Subsequence Widths
# https://leetcode.com/problems/sum-of-subsequence-widths/

# @param {Integer[]} nums
# @return {Integer}
def sum_subseq_widths(nums)
  mod = 10**9 + 7
  nums.sort!
  n = nums.length
  pow2 = Array.new(n, 1)
  (1...n).each { |i| pow2[i] = (pow2[i - 1] * 2) % mod }
  ans = 0
  nums.each_with_index do |x, i|
    ans = (ans + x * (pow2[i] - pow2[n - 1 - i])) % mod
  end
  ans
end
