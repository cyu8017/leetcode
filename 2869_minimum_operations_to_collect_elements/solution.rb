# LeetCode 2869 - Minimum Operations to Collect Elements
# https://leetcode.com/problems/minimum-operations-to-collect-elements/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_operations(nums, k)
  need = {}
  (1..k).each { |x| need[x] = true }
  (nums.length - 1).downto(0) do |i|
    need.delete(nums[i])
    return nums.length - i if need.empty?
  end
  nums.length
end
