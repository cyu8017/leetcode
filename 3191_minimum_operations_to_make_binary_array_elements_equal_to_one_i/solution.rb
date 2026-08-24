# LeetCode 3191 - Minimum Operations to Make Binary Array Elements Equal to One I
# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/

# @param {Integer[]} nums
# @return {Integer}
def min_operations(nums)
  ans = 0
  nums.each_index do |i|
    next if nums[i] != 0
    return -1 if i + 2 >= nums.length
    nums[i + 1] ^= 1
    nums[i + 2] ^= 1
    ans += 1
  end
  ans
end
