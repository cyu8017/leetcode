# LeetCode 0098 - Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @return {Boolean}
def is_valid_bst(root)
  valid = lambda do |node, low, high|
    return true if node.nil?
    return false unless low < node.val && node.val < high

    valid.call(node.left, low, node.val) && valid.call(node.right, node.val, high)
  end

  valid.call(root, -Float::INFINITY, Float::INFINITY)
end
