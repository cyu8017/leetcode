# LeetCode 2936 - Number of Equal Numbers Blocks
# https://leetcode.com/problems/number-of-equal-numbers-blocks/

# @param {Integer[]} nums
# @return {Integer}
def block_count(nums)
  return 0 if nums.empty?

  ans = 1
  (1...nums.length).each { |i| ans += 1 if nums[i] != nums[i - 1] }
  ans
end
