# LeetCode 2236 - Root Equals Sum of Children
# https://leetcode.com/problems/root-equals-sum-of-children/

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
def check_tree(root)
  root.val == root.left.val + root.right.val
end
