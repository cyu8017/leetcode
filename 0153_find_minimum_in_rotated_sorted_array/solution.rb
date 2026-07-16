# LeetCode 0153 - Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution
  def find_min(nums)
    left = 0
    right = nums.length - 1
    while left < right
      middle = (left + right) / 2
      if nums[middle] > nums[right]
        left = middle + 1
      else
        right = middle
      end
    end
    nums[left]
  end
end