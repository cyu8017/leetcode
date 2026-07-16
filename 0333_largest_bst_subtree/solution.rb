# LeetCode 0333 - Largest BST Subtree
# https://leetcode.com/problems/largest-bst-subtree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

class Solution
  def largest_bst_subtree(root)
    root = list_to_tree(root) if root.is_a?(Array)
    @best = 0

    dfs = lambda do |node|
      return [true, 10**9, -(10**9), 0] if node.nil?

      left_ok, left_min, left_max, left_size = dfs.call(node.left)
      right_ok, right_min, right_max, right_size = dfs.call(node.right)

      if left_ok && right_ok && left_max < node.val && node.val < right_min
        size = left_size + right_size + 1
        @best = [@best, size].max
        return [true, [left_min, node.val].min, [right_max, node.val].max, size]
      end

      [false, 0, 0, 0]
    end

    dfs.call(root)
    @best
  end

  alias_method :largestBSTSubtree, :largest_bst_subtree

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
