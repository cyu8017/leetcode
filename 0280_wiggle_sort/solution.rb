# LeetCode 0280 - Wiggle Sort
# https://leetcode.com/problems/wiggle-sort/

class Solution
  def wiggleSort(nums)
    (1...nums.length - 1).each do |index|
      if index.odd? && nums[index] < nums[index - 1]
        nums[index], nums[index - 1] = nums[index - 1], nums[index]
      elsif index.even? && nums[index] > nums[index - 1]
        nums[index], nums[index - 1] = nums[index - 1], nums[index]
      end
    end
    nums
  end
end
