# LeetCode 1509 - Minimum Difference Between Largest and Smallest Value in Three Moves
# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

# @param {Integer[]} nums
# @return {Integer}
def min_difference(nums)
  return 0 if nums.length <= 4
  nums = nums.sort
  (0...4).map { |i| nums[-4 + i] - nums[i] }.min
end
