# LeetCode 0104 - Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

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
def max_depth(root)
  return 0 if root.nil?

  1 + [max_depth(root.left), max_depth(root.right)].max
end