# LeetCode 0998 - Maximum Binary Tree II
# https://leetcode.com/problems/maximum-binary-tree-ii/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @param {Integer} val
# @return {TreeNode}
def insert_into_max_tree(root, val)
  if root.nil? || val > root.val
    node = TreeNode.new(val)
    node.left = root
    return node
  end
  root.right = insert_into_max_tree(root.right, val)
  root
end
