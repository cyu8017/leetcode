# LeetCode 0543 - Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

class Solution
  def diameter_of_binary_tree(root)
    @best = 0

    depth = lambda do |node|
      return 0 if node.nil?

      left = depth.call(node.left)
      right = depth.call(node.right)
      @best = [@best, left + right].max
      1 + [left, right].max
    end

    depth.call(root)
    @best
  end

  alias_method :diameterOfBinaryTree, :diameter_of_binary_tree
end
