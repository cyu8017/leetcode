# LeetCode 1748 - Sum of Unique Elements
# https://leetcode.com/problems/sum-of-unique-elements/

# @param {Integer[]} nums
# @return {Integer}
def sum_of_unique(nums)
  counts = Hash.new(0)
  nums.each { |value| counts[value] += 1 }
  counts.sum { |value, count| count == 1 ? value : 0 }
end
