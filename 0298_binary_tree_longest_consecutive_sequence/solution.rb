# LeetCode 0298 - Binary Tree Longest Consecutive Sequence
# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

class Solution
  def longestConsecutive(root)
    dfs = lambda do |node, parent, length|
      return 0 if node.nil?

      current = parent && parent.val + 1 == node.val ? length + 1 : 1
      [
        current,
        dfs.call(node.left, node, current),
        dfs.call(node.right, node, current)
      ].max
    end

    dfs.call(root, nil, 0)
  end
end
