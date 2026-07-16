# LeetCode 0034 - Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def search_range(nums, target)
  lower_bound = lambda do
    left = 0
    right = nums.length
    while left < right
      mid = (left + right) / 2
      if nums[mid] < target
        left = mid + 1
      else
        right = mid
      end
    end
    left
  end

  upper_bound = lambda do
    left = 0
    right = nums.length
    while left < right
      mid = (left + right) / 2
      if nums[mid] <= target
        left = mid + 1
      else
        right = mid
      end
    end
    left
  end

  return [-1, -1] if nums.empty?

  start = lower_bound.call
  return [-1, -1] if start == nums.length || nums[start] != target

  [start, upper_bound.call - 1]
end
