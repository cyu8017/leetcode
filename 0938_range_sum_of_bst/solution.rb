# LeetCode 0938 - Range Sum of BST
# https://leetcode.com/problems/range-sum-of-bst/

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
# @return {Integer}
def range_sum_bst(root, low, high)
  return 0 if root.nil?
  return range_sum_bst(root.right, low, high) if root.val < low
  return range_sum_bst(root.left, low, high) if root.val > high

  root.val + range_sum_bst(root.left, low, high) + range_sum_bst(root.right, low, high)
end
