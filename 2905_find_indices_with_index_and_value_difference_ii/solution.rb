# LeetCode 2905 - Find Indices With Index and Value Difference II
# https://leetcode.com/problems/find-indices-with-index-and-value-difference-ii/

# @param {Integer[]} nums
# @param {Integer} index_difference
# @param {Integer} value_difference
# @return {Integer[]}
def find_indices(nums, index_difference, value_difference)
  n = nums.length
  min_idx = 0
  max_idx = 0
  (index_difference...n).each do |j|
    i = j - index_difference
    min_idx = i if nums[i] < nums[min_idx]
    max_idx = i if nums[i] > nums[max_idx]
    return [min_idx, j] if nums[j] - nums[min_idx] >= value_difference
    return [max_idx, j] if nums[max_idx] - nums[j] >= value_difference
  end
  [-1, -1]
end
