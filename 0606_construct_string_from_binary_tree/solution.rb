# LeetCode 0606 - Construct String from Binary Tree
# https://leetcode.com/problems/construct-string-from-binary-tree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @return {String}
def tree2str(root)
  return "" if root.nil?

  result = root.val.to_s
  result += "(#{tree2str(root.left)})" if root.left || root.right
  result += "(#{tree2str(root.right)})" if root.right
  result
end
