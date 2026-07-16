# LeetCode 0199 - Binary Tree Right Side View
class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

class Solution
  def right_side_view(root)
    return [] unless root

    result = []
    queue = [root]
    until queue.empty?
      level_size = queue.length
      level_size.times do |index|
        node = queue.shift
        result << node.val if index == level_size - 1
        queue << node.left if node.left
        queue << node.right if node.right
      end
    end
    result
  end
end