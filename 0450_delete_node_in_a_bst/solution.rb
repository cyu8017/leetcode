# LeetCode 0450 - Delete Node in a BST
# https://leetcode.com/problems/delete-node-in-a-bst/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

class Solution
  def delete_node(root, key)
    return nil if root.nil?
    if key < root.val
      root.left = delete_node(root.left, key)
    elsif key > root.val
      root.right = delete_node(root.right, key)
    else
      return root.right if root.left.nil?
      return root.left if root.right.nil?

      successor = root.right
      successor = successor.left while successor.left
      root.val = successor.val
      root.right = delete_node(root.right, successor.val)
    end
    root
  end

  alias_method :deleteNode, :delete_node
end
