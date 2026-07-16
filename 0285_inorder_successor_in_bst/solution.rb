# LeetCode 0285 - Inorder Successor in BST
# https://leetcode.com/problems/inorder-successor-in-bst/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

class Solution
  def inorderSuccessor(root, p)
    if p.right
      current = p.right
      current = current.left while current.left
      return current
    end
    successor = nil
    current = root
    while current
      if p.val < current.val
        successor = current
        current = current.left
      else
        current = current.right
      end
    end
    successor
  end
end
