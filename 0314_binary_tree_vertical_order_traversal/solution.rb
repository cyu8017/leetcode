# LeetCode 0314 - Binary Tree Vertical Order Traversal
# https://leetcode.com/problems/binary-tree-vertical-order-traversal/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

class Solution
  def verticalOrder(root)
    return [] if root.nil?

    columns = Hash.new { |hash, key| hash[key] = [] }
    queue = [[root, 0]]
    min_col = 0
    max_col = 0
    until queue.empty?
      node, column = queue.shift
      min_col = [min_col, column].min
      max_col = [max_col, column].max
      columns[column] << node.val
      queue << [node.left, column - 1] if node.left
      queue << [node.right, column + 1] if node.right
    end
    (min_col..max_col).map { |column| columns[column] }
  end
end
