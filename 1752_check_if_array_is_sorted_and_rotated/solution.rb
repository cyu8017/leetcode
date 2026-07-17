# LeetCode 1752 - Check if Array Is Sorted and Rotated
# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

# @param {Integer[]} nums
# @return {Boolean}
def check(nums)
  n = nums.length
  drops = (0...n).count { |i| nums[i] > nums[(i + 1) % n] }
  drops <= 1
end
