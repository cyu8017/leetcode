# LeetCode 0637 - Average of Levels in Binary Tree
# https://leetcode.com/problems/average-of-levels-in-binary-tree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @return {Float[]}
def average_of_levels(root)
  return [] if root.nil?

  result = []
  queue = [root]
  until queue.empty?
    total = 0.0
    count = queue.length
    count.times do
      node = queue.shift
      total += node.val
      queue << node.left if node.left
      queue << node.right if node.right
    end
    result << total / count
  end
  result
end
