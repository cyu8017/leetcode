# LeetCode 0814 - Binary Tree Pruning
# https://leetcode.com/problems/binary-tree-pruning/

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
def prune_tree(root)
  return nil if root.nil?

  root.left = prune_tree(root.left)
  root.right = prune_tree(root.right)
  return nil if root.val == 0 && root.left.nil? && root.right.nil?

  root
end
