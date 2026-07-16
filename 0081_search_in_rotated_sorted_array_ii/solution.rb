# LeetCode 0081 - Search in Rotated Sorted Array II
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

# @param {Integer[]} nums
# @param {Integer} target
# @return {Boolean}
def search(nums, target)
  left = 0
  right = nums.length - 1

  while left <= right
    mid = (left + right) / 2
    return true if nums[mid] == target

    if nums[left] == nums[mid] && nums[mid] == nums[right]
      left += 1
      right -= 1
    elsif nums[left] <= nums[mid]
      if nums[left] <= target && target < nums[mid]
        right = mid - 1
      else
        left = mid + 1
      end
    elsif nums[mid] < target && target <= nums[right]
      left = mid + 1
    else
      right = mid - 1
    end
  end

  false
end
