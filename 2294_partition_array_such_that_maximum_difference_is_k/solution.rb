# LeetCode 2294 - Partition Array Such That Maximum Difference Is K
# https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def partition_array(nums, k)
  nums = nums.sort
  ans = 1
  start = nums[0]
  (1...nums.length).each do |i|
    if nums[i] - start > k
      ans += 1
      start = nums[i]
    end
  end
  ans
end
