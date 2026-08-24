# LeetCode 0915 - Partition Array Into Disjoint Intervals
# https://leetcode.com/problems/partition-array-into-disjoint-intervals/

# @param {Integer[]} nums
# @return {Integer}
def partition_disjoint(nums)
  max_left = nums[0]
  (1...nums.length).each do |i|
    return i if max_left <= nums[i..].min

    max_left = [max_left, nums[i]].max
  end
  nums.length - 1
end
