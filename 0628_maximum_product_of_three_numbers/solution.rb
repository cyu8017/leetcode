# LeetCode 0628 - Maximum Product of Three Numbers
# https://leetcode.com/problems/maximum-product-of-three-numbers/

# @param {Integer[]} nums
# @return {Integer}
def maximum_product(nums)
  nums.sort!
  [nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1]].max
end
