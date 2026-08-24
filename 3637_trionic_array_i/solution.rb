# LeetCode 3637 - Trionic Array I
# https://leetcode.com/problems/trionic-array-i/

# @param {Integer[]} nums
# @return {Boolean}
def is_trionic(nums)
  n = nums.length
  p = 0
  p += 1 while p < n - 2 && nums[p] < nums[p + 1]
  return false if p == 0

  q = p
  q += 1 while q < n - 1 && nums[q] > nums[q + 1]
  return false if q == p || q == n - 1

  q += 1 while q < n - 1 && nums[q] < nums[q + 1]
  q == n - 1
end
