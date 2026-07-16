# LeetCode 0101 - Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/

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
def is_symmetric(root)
  return true if root.nil?

  mirrors(root.left, root.right)
end

def mirrors(left, right)
  return true if left.nil? && right.nil?
  return false if left.nil? || right.nil? || left.val != right.val

  mirrors(left.left, right.right) && mirrors(left.right, right.left)
end
