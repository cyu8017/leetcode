# LeetCode 0540 - Single Element in a Sorted Array
# https://leetcode.com/problems/single-element-in-a-sorted-array/

class Solution
  def single_non_duplicate(nums)
    left = 0
    right = nums.length - 1

    while left < right
      mid = (left + right) / 2
      mid -= 1 if mid.odd?
      if nums[mid] == nums[mid + 1]
        left = mid + 2
      else
        right = mid
      end
    end

    nums[left]
  end

  alias_method :singleNonDuplicate, :single_non_duplicate
end
