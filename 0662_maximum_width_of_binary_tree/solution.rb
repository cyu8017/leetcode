# LeetCode 0662 - Maximum Width of Binary Tree
# https://leetcode.com/problems/maximum-width-of-binary-tree/

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
def width_of_binary_tree(root)
  return 0 if root.nil?

  queue = [[root, 0]]
  best = 0
  until queue.empty?
    left = queue[0][1]
    queue.length.times do
      node, idx = queue.shift
      best = [best, idx - left + 1].max
      queue << [node.left, idx * 2] if node.left
      queue << [node.right, idx * 2 + 1] if node.right
    end
  end
  best
end
