# LeetCode 0094 - Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @return {Integer[]}
def inorder_traversal(root)
  result = []
  stack = []
  current = root
  while current || !stack.empty?
    while current
      stack << current
      current = current.left
    end
    current = stack.pop
    result << current.val
    current = current.right
  end
  result
end
