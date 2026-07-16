# LeetCode 0110 - Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/

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
def is_balanced(root)
  height(root) != -1
end

def height(node)
  return 0 if node.nil?

  left = height(node.left)
  return -1 if left == -1

  right = height(node.right)
  return -1 if right == -1

  return -1 if (left - right).abs > 1

  1 + [left, right].max
end
