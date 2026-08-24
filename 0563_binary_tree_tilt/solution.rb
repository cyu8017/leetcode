# LeetCode 0563 - Binary Tree Tilt
# https://leetcode.com/problems/binary-tree-tilt/

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
def find_tilt(root)
  total = 0

  subtree_sum = lambda do |node|
    return 0 if node.nil?

    left = subtree_sum.call(node.left)
    right = subtree_sum.call(node.right)
    total += (left - right).abs
    node.val + left + right
  end

  subtree_sum.call(root)
  total
end
