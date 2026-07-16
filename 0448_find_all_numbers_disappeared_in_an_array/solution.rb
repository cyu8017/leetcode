# LeetCode 0448 - Find All Numbers Disappeared in an Array
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution
  def find_disappeared_numbers(nums)
    nums.each do |number|
      index = number.abs - 1
      nums[index] = -nums[index] if nums[index].positive?
    end
    nums.each_with_index.filter_map { |value, index| index + 1 if value.positive? }
  end

  alias_method :findDisappearedNumbers, :find_disappeared_numbers
end
