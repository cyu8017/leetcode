# LeetCode 0669 - Trim a Binary Search Tree
# https://leetcode.com/problems/trim-a-binary-search-tree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @param {Integer} low
# @param {Integer} high
# @return {TreeNode}
def trim_bst(root, low, high)
  return nil if root.nil?
  return trim_bst(root.right, low, high) if root.val < low
  return trim_bst(root.left, low, high) if root.val > high

  root.left = trim_bst(root.left, low, high)
  root.right = trim_bst(root.right, low, high)
  root
end
