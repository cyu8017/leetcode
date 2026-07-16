# LeetCode 0162 - Find Peak Element
# https://leetcode.com/problems/find-peak-element/

class Solution
  def find_peak_element(nums)
    left = 0
    right = nums.length - 1
    while left < right
      mid = left + (right - left) / 2
      nums[mid] > nums[mid + 1] ? right = mid : left = mid + 1
    end
    left
end