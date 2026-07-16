# LeetCode 0404 - Sum of Left Leaves
# https://leetcode.com/problems/sum-of-left-leaves/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

class Solution
  def sum_of_left_leaves(root)
    return 0 if root.nil?

    total = 0
    if root.left && root.left.left.nil? && root.left.right.nil?
      total += root.left.val
    else
      total += sum_of_left_leaves(root.left)
    end

    total + sum_of_left_leaves(root.right)
  end

  alias_method :sumOfLeftLeaves, :sum_of_left_leaves
end
