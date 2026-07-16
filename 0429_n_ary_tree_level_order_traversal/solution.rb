# LeetCode 0429 - N-ary Tree Level Order Traversal
# https://leetcode.com/problems/n-ary-tree-level-order-traversal/

class Node
  attr_accessor :val, :children

  def initialize(val = nil, children = nil)
    @val = val
    @children = children || []
  end
end

class Solution
  def level_order(root)
    return [] if root.nil?

    result = []
    queue = [root]

    until queue.empty?
      level = []
      queue.length.times do
        node = queue.shift
        level << node.val
        queue.concat(node.children)
      end
      result << level
    end

    result
  end

  alias_method :levelOrder, :level_order
end
