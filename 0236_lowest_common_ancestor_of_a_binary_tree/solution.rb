# LeetCode 0236 - Lowest Common Ancestor of a Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @param {TreeNode} p
# @param {TreeNode} q
# @return {TreeNode}
def lowest_common_ancestor(root, p, q)
  return root if root.nil? || root.equal?(p) || root.equal?(q)

  left = lowest_common_ancestor(root.left, p, q)
  right = lowest_common_ancestor(root.right, p, q)
  return root if left && right

  left || right
end
