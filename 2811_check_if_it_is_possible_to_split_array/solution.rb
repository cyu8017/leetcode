# LeetCode 2811 - Check if it is Possible to Split Array
# https://leetcode.com/problems/check-if-it-is-possible-to-split-array/

# @param {Integer[]} nums
# @param {Integer} m
# @return {Boolean}
def can_split_array(nums, m)
  n = nums.length
  return true if n <= 2
  (0...(n - 1)).each { |i| return true if nums[i] + nums[i + 1] >= m }
  false
end
