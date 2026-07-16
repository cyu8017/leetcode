# LeetCode 0189 - Rotate Array
# https://leetcode.com/problems/rotate-array/

# @param {Integer[]} nums
# @param {Integer} k
# @return {void}
def rotate(nums, k)
  k %= nums.length
  reverse_range(nums, 0, nums.length - 1)
  reverse_range(nums, 0, k - 1)
  reverse_range(nums, k, nums.length - 1)
end

def reverse_range(nums, left, right)
  while left < right
    nums[left], nums[right] = nums[right], nums[left]
    left += 1
    right -= 1
  end
end