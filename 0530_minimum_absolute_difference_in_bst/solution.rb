# LeetCode 0530 - Minimum Absolute Difference in BST
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

class Solution
  def get_minimum_difference(root)
    @previous = nil
    @best = Float::INFINITY
    inorder(root)
    @best
  end

  alias_method :getMinimumDifference, :get_minimum_difference

  private

  def inorder(node)
    return if node.nil?

    inorder(node.left)
    if @previous
      @best = [@best, node.val - @previous].min
    end
    @previous = node.val
    inorder(node.right)
  end
end
