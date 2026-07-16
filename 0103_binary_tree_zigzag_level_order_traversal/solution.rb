# LeetCode 0103 - Binary Tree Zigzag Level Order Traversal
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

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
def zigzag_level_order(root)
  return [] if root.nil?

  result = []
  queue = [root]
  left_to_right = true

  until queue.empty?
    size = queue.length
    level = []
    size.times do
      node = queue.shift
      level << node.val
      queue << node.left if node.left
      queue << node.right if node.right
    end
    level.reverse! unless left_to_right
    result << level
    left_to_right = !left_to_right
  end

  result
end
