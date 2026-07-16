# LeetCode 0545 - Boundary of Binary Tree
# https://leetcode.com/problems/boundary-of-binary-tree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

class Solution
  def boundary_of_binary_tree(root)
    return [] if root.nil?

    leaf = lambda do |node|
      !node.nil? && node.left.nil? && node.right.nil?
    end

    left_boundary = lambda do |node|
      return [] if node.nil? || leaf.call(node)

      if node.left
        [node.val] + left_boundary.call(node.left)
      else
        [node.val] + left_boundary.call(node.right)
      end
    end

    right_boundary = lambda do |node|
      return [] if node.nil? || leaf.call(node)

      if node.right
        right_boundary.call(node.right) + [node.val]
      else
        right_boundary.call(node.left) + [node.val]
      end
    end

    leaves = lambda do |node|
      return [] if node.nil?
      return [node.val] if leaf.call(node)

      leaves.call(node.left) + leaves.call(node.right)
    end

    return [root.val] if leaf.call(root)

    [root.val] + left_boundary.call(root.left) + leaves.call(root) + right_boundary.call(root.right)
  end

  alias_method :boundaryOfBinaryTree, :boundary_of_binary_tree
end
