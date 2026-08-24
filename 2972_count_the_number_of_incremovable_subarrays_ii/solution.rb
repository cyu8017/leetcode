# LeetCode 2972 - Count the Number of Incremovable Subarrays II
# https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-ii/

# @param {Integer[]} nums
# @return {Integer}
def incremovable_subarray_count(nums)
  n = nums.length
  left = 0
  left += 1 while left + 1 < n && nums[left] < nums[left + 1]
  return n * (n + 1) / 2 if left == n - 1

  ans = left + 2
  right = n - 1
  while right > 0 && (right == n - 1 || nums[right] < nums[right + 1])
    left -= 1 while left >= 0 && nums[left] >= nums[right]
    ans += left + 2
    right -= 1
    break if right > 0 && nums[right] >= nums[right + 1]
  end
  ans
end
