# LeetCode 0169 - Majority Element
# https://leetcode.com/problems/majority-element/

class Solution
  def majority_element(nums)
    candidate = nil
    count = 0
    nums.each do |number|
      candidate = number if count.zero?
      count += number == candidate ? 1 : -1
    end
    candidate
  end
end