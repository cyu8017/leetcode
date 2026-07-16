# LeetCode 0156 - Binary Tree Upside Down
# https://leetcode.com/problems/binary-tree-upside-down/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

class Solution
  def upside_down_binary_tree(root)
    previous = nil
    previous_right = nil
    current = root
    while current
      next_node = current.left
      current.left = previous_right
      previous_right = current.right
      current.right = previous
      previous = current
      current = next_node
    end
    previous
  end
end