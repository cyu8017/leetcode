# LeetCode 2779 - Maximum Beauty of an Array After Applying Operation
# https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximum_beauty(nums, k)
  nums = nums.sort
  ans = 0
  left = 0
  (0...nums.length).each do |right|
    left += 1 while nums[right] - nums[left] > 2 * k
    ans = [ans, right - left + 1].max
  end
  ans
end
