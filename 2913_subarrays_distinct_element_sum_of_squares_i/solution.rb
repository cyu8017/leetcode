# LeetCode 2913 - Subarrays Distinct Element Sum of Squares I
# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/

# @param {Integer[]} nums
# @return {Integer}
def sum_counts(nums)
  n = nums.length
  ans = 0
  (0...n).each do |i|
    seen = {}
    (i...n).each do |j|
      seen[nums[j]] = true
      d = seen.length
      ans += d * d
    end
  end
  ans
end
