# LeetCode 0124 - Binary Tree Maximum Path Sum
# https://leetcode.com/problems/binary-tree-maximum-path-sum/

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
def max_path_sum(root)
  best = -Float::INFINITY
  gain = lambda do |node|
    next 0 if node.nil?

    left = [gain.call(node.left), 0].max
    right = [gain.call(node.right), 0].max
    best = [best, node.val + left + right].max
    node.val + [left, right].max
  end
  gain.call(root)
  best
end