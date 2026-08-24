# LeetCode 0572 - Subtree of Another Tree
# https://leetcode.com/problems/subtree-of-another-tree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @param {TreeNode} sub_root
# @return {Boolean}
def is_subtree(root, sub_root)
  same = lambda do |a, b|
    return a.equal?(b) || (a.nil? && b.nil?) if a.nil? || b.nil?

    a.val == b.val && same.call(a.left, b.left) && same.call(a.right, b.right)
  end

  return false if root.nil?

  same.call(root, sub_root) || is_subtree(root.left, sub_root) || is_subtree(root.right, sub_root)
end
