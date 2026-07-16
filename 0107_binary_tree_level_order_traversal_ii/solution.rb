# LeetCode 0107 - Binary Tree Level Order Traversal II
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

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
def level_order_bottom(root)
  return [] if root.nil?

  result = []
  queue = [root]

  until queue.empty?
    level = []
    queue.size.times do
      node = queue.shift
      level << node.val
      queue << node.left if node.left
      queue << node.right if node.right
    end
    result << level
  end

  result.reverse
end
