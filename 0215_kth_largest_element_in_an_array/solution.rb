# LeetCode 0215 - Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/

class Solution
  def find_kth_largest(nums, k)
    target = nums.length - k
    left = 0
    right = nums.length - 1
    while left <= right
      pivot_index = partition(nums, left, right)
      return nums[pivot_index] if pivot_index == target

      if pivot_index < target
        left = pivot_index + 1
      else
        right = pivot_index - 1
      end
    end
    nums[left]
  end

  private

  def partition(nums, left, right)
    pivot_index = left + rand(right - left + 1)
    nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
    store = left
    (left...right).each do |i|
      if nums[i] <= nums[right]
        nums[store], nums[i] = nums[i], nums[store]
        store += 1
      end
    end
    nums[store], nums[right] = nums[right], nums[store]
    store
  end
end
