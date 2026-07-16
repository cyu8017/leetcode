# LeetCode 0337 - House Robber III
# https://leetcode.com/problems/house-robber-iii/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

class Solution
  def rob(root)
    root = list_to_tree(root) if root.is_a?(Array)

    dfs = lambda do |node|
      return [0, 0] if node.nil?

      left_with, left_without = dfs.call(node.left)
      right_with, right_without = dfs.call(node.right)

      with_rob = node.val + left_without + right_without
      without_rob = [left_with, left_without].max + [right_with, right_without].max
      [with_rob, without_rob]
    end

    dfs.call(root).max
  end

  private

  def list_to_tree(values)
    return nil if values.nil? || values.empty?

    root = TreeNode.new(values[0])
    queue = [root]
    index = 1
    while index < values.length
      node = queue.shift
      if index < values.length && !values[index].nil?
        node.left = TreeNode.new(values[index])
        queue << node.left
      end
      index += 1
      if index < values.length && !values[index].nil?
        node.right = TreeNode.new(values[index])
        queue << node.right
      end
      index += 1
    end
    root
  end
end
