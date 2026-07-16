# LeetCode 0510 - Inorder Successor in BST II
# https://leetcode.com/problems/inorder-successor-in-bst-ii/

class Node
  attr_accessor :val, :left, :right, :parent

  def initialize(val = 0, left = nil, right = nil, parent = nil)
    @val = val
    @left = left
    @right = right
    @parent = parent
  end
end

class Solution
  def inorder_successor(node)
    if node.right
      current = node.right
      current = current.left while current.left
      return current
    end

    current = node
    while current.parent && current.equal?(current.parent.right)
      current = current.parent
    end
    current.parent
  end

  alias_method :inorderSuccessor, :inorder_successor
end
