# LeetCode 0238 - Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/

# @param {Integer[]} nums
# @return {Integer[]}
def product_except_self(nums)
  length = nums.length
  result = Array.new(length, 1)
  prefix = 1
  (0...length).each do |index|
    result[index] = prefix
    prefix *= nums[index]
  end
  suffix = 1
  (length - 1).downto(0) do |index|
    result[index] *= suffix
    suffix *= nums[index]
  end
  result
end
