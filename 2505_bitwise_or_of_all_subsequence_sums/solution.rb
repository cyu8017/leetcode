# LeetCode 2505 - Bitwise OR of All Subsequence Sums
# https://leetcode.com/problems/bitwise-or-of-all-subsequence-sums/

# @param {Integer[]} nums
# @return {Integer}
def subsequence_sum_or(nums)
  ans = 0
  prefix = 0
  nums.each do |x|
    prefix += x
    ans |= x | prefix
  end
  ans
end
