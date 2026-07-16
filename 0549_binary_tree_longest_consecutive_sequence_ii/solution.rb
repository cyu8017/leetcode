# LeetCode 0549 - Binary Tree Longest Consecutive Sequence II
# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

class Solution
  def longest_consecutive(root)
    @best = 0

    dfs = lambda do |node|
      return [0, 0] if node.nil?

      left_inc, left_dec = dfs.call(node.left)
      right_inc, right_dec = dfs.call(node.right)

      inc = 1
      dec = 1
      if node.left
        inc = [inc, left_inc + 1].max if node.left.val == node.val + 1
        dec = [dec, left_dec + 1].max if node.left.val == node.val - 1
      end
      if node.right
        inc = [inc, right_inc + 1].max if node.right.val == node.val + 1
        dec = [dec, right_dec + 1].max if node.right.val == node.val - 1
      end

      if node.left && node.right
        if node.left.val + 1 == node.val && node.val == node.right.val - 1
          @best = [@best, left_dec + 1 + right_inc].max
        end
        if node.left.val - 1 == node.val && node.val == node.right.val + 1
          @best = [@best, left_inc + 1 + right_dec].max
        end
      end

      @best = [@best, inc, dec].max
      [inc, dec]
    end

    dfs.call(root)
    @best
  end

  alias_method :longestConsecutive, :longest_consecutive
end
