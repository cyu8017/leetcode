# LeetCode 0102 - Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @return {Integer[][]}
def level_order(root)
  return [] if root.nil?

  result = []
  queue = [root]

  until queue.empty?
    size = queue.length
    level = []
    size.times do
      node = queue.shift
      level << node.val
      queue << node.left if node.left
      queue << node.right if node.right
    end
    result << level
  end

  result
end
