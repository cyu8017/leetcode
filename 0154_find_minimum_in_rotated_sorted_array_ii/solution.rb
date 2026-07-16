# LeetCode 0154 - Find Minimum in Rotated Sorted Array II
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

class Solution
  def find_min(nums)
    left = 0
    right = nums.length - 1
    while left < right
      middle = (left + right) / 2
      if nums[middle] > nums[right]
        left = middle + 1
      elsif nums[middle] < nums[right]
        right = middle
      else
        right -= 1
      end
    end
    nums[left]
  end
end