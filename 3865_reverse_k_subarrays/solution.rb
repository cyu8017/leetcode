# LeetCode 3865 - Reverse K Subarrays
# https://leetcode.com/problems/reverse-k-subarrays/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def reverse_subarrays(nums, k)
  n = nums.length
  m = n / k
  i = 0
  while i < n
    lo = i
    hi = i + m - 1
    while lo < hi
      nums[lo], nums[hi] = nums[hi], nums[lo]
      lo += 1
      hi -= 1
    end
    i += m
  end
  nums
end
