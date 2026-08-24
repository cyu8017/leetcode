# LeetCode 0918 - Maximum Sum Circular Subarray
# https://leetcode.com/problems/maximum-sum-circular-subarray/

# @param {Integer[]} nums
# @return {Integer}
def max_subarray_sum_circular(nums)
  total = nums.sum
  max_sum = min_sum = cur_max = cur_min = nums[0]
  nums[1..].each do |x|
    cur_max = [x, cur_max + x].max
    cur_min = [x, cur_min + x].min
    max_sum = [max_sum, cur_max].max
    min_sum = [min_sum, cur_min].min
  end
  return max_sum if max_sum < 0

  [max_sum, total - min_sum].max
end
