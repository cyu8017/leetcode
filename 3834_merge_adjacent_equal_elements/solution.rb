# LeetCode 3834 - Merge Adjacent Equal Elements
# https://leetcode.com/problems/merge-adjacent-equal-elements/

# @param {Integer[]} nums
# @return {Integer[]}
def merge_adjacent(nums)
  stk = []
  nums.each do |x|
    stk << x
    while stk.length > 1 && stk[-1] == stk[-2]
      a = stk.pop
      b = stk.pop
      stk << a + b
    end
  end
  stk
end
