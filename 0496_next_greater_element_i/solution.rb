# LeetCode 0496 - Next Greater Element I
# https://leetcode.com/problems/next-greater-element-i/

class Solution
  def next_greater_element(nums1, nums2)
    next_greater = {}
    stack = []
    nums2.each do |num|
      while !stack.empty? && stack[-1] < num
        next_greater[stack.pop] = num
      end
      stack << num
    end
    nums1.map { |num| next_greater.fetch(num, -1) }
  end

  alias_method :nextGreaterElement, :next_greater_element
end
