# LeetCode 0366 - Find Leaves of Binary Tree
# https://leetcode.com/problems/find-leaves-of-binary-tree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

class Solution
  def find_leaves(root)
    root = list_to_tree(root) if root.is_a?(Array)
    layers = []

    dfs = lambda do |node|
      return -1 if node.nil?

      height = [dfs.call(node.left), dfs.call(node.right)].max + 1
      layers << [] while layers.length <= height
      layers[height] << node.val
      height
    end

    dfs.call(root)
    layers
  end

  alias_method :findLeaves, :find_leaves

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
