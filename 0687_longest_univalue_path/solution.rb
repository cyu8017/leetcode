# LeetCode 0687 - Longest Univalue Path
# https://leetcode.com/problems/longest-univalue-path/

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
def longest_univalue_path(root)
  best = 0

  dfs = lambda do |node|
    return 0 if node.nil?

    left = dfs.call(node.left)
    right = dfs.call(node.right)
    left_path = node.left && node.left.val == node.val ? left + 1 : 0
    right_path = node.right && node.right.val == node.val ? right + 1 : 0
    best = [best, left_path + right_path].max
    [left_path, right_path].max
  end

  dfs.call(root)
  best
end
