# LeetCode 1911 - Maximum Alternating Subsequence Sum
# https://leetcode.com/problems/maximum-alternating-subsequence-sum/

# @param {Integer[]} nums
# @return {Integer}
def max_alternating_sum(nums)
  even = odd = 0
  nums.each do |x|
    even, odd = [even, odd + x].max, [odd, even - x].max
  end
  even
end
