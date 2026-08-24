# LeetCode 2057 - Smallest Index With Equal Value
# https://leetcode.com/problems/smallest-index-with-equal-value/

# @param {Integer[]} nums
# @return {Integer}
def smallest_equal(nums)
  nums.each_with_index { |v, i| return i if i % 10 == v }
  -1
end
