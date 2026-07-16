# LeetCode 0538 - Convert BST to Greater Tree
# https://leetcode.com/problems/convert-bst-to-greater-tree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

class Solution
  def convert_bst(root)
    @running = 0
    reverse_inorder(root)
  end

  alias_method :convertBST, :convert_bst

  private

  def reverse_inorder(node)
    return if node.nil?

    reverse_inorder(node.right)
    @running += node.val
    node.val = @running
    reverse_inorder(node.left)
  end
end
