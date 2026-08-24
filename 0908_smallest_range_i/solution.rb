# LeetCode 0908 - Smallest Range I
# https://leetcode.com/problems/smallest-range-i/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def smallest_range_i(nums, k)
  [0, nums.max - nums.min - 2 * k].max
end
