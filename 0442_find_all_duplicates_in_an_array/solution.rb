# LeetCode 0442 - Find All Duplicates in an Array
# https://leetcode.com/problems/find-all-duplicates-in-an-array/

class Solution
  def find_duplicates(nums)
    result = []
    nums.each do |number|
      index = number.abs - 1
      if nums[index].negative?
        result << number.abs
      else
        nums[index] = -nums[index]
      end
    end
    result
  end

  alias_method :findDuplicates, :find_duplicates
end
