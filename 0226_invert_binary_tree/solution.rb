# LeetCode 0226 - Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @return {TreeNode}
def invert_tree(root)
  return nil if root.nil?

  left = invert_tree(root.left)
  right = invert_tree(root.right)
  root.left = right
  root.right = left
  root
end
