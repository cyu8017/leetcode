# LeetCode 0561 - Array Partition
# https://leetcode.com/problems/array-partition/

# @param {Integer[]} nums
# @return {Integer}
def array_pair_sum(nums)
  nums.sort.each_slice(2).sum(&:first)
end
