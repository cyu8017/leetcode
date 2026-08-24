# LeetCode 0783 - Minimum Distance Between BST Nodes
# https://leetcode.com/problems/minimum-distance-between-bst-nodes/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @return {Integer}
def min_diff_in_bst(root)
  prev = nil
  best = Float::INFINITY

  inorder = lambda do |node|
    return if node.nil?

    inorder.call(node.left)
    best = [best, node.val - prev].min unless prev.nil?
    prev = node.val
    inorder.call(node.right)
  end

  inorder.call(root)
  best.to_i
end
