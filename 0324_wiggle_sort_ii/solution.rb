# LeetCode 0324 - Wiggle Sort II
# https://leetcode.com/problems/wiggle-sort-ii/

class Solution
  def wiggleSort(nums)
    sorted_nums = nums.sort
    left = (nums.length - 1) / 2
    right = nums.length - 1
    nums.each_index do |index|
      if index.even?
        nums[index] = sorted_nums[left]
        left -= 1
      else
        nums[index] = sorted_nums[right]
        right -= 1
      end
    end
    nums
  end
end
