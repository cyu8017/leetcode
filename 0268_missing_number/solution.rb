# LeetCode 0268 - Missing Number
# https://leetcode.com/problems/missing-number/

# @param {Integer[]} nums
# @return {Integer}
def missing_number(nums)
  length = nums.length
  expected = length * (length + 1) / 2
  expected - nums.sum
end
