# LeetCode 3423 - Maximum Difference Between Adjacent Elements in a Circular Array
# https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/

# @param {Integer[]} nums
# @return {Integer}
def max_adjacent_distance(nums)
  ans = 0
  n = nums.length
  (0...n).each do |i|
    d = (nums[i] - nums[(i + 1) % n]).abs
    ans = d if d > ans
  end
  ans
end
