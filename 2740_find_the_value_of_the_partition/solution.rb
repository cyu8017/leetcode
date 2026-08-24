# LeetCode 2740 - Find the Value of the Partition
# https://leetcode.com/problems/find-the-value-of-the-partition/

# @param {Integer[]} nums
# @return {Integer}
def find_value_of_partition(nums)
  nums = nums.sort
  ans = 10**18
  (1...nums.length).each { |i| ans = [ans, nums[i] - nums[i - 1]].min }
  ans
end
