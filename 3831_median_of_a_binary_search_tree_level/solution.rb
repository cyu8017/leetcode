# LeetCode 3831 - Median of a Binary Search Tree Level
# https://leetcode.com/problems/median-of-a-binary-search-tree-level/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @param {Integer} level
# @return {Integer}
def level_median(root, level)
  nums = []
  dfs = nil
  dfs = lambda do |node, i|
    return if node.nil?
    dfs.call(node.left, i + 1)
    nums << node.val if i == level
    dfs.call(node.right, i + 1)
  end
  dfs.call(root, 0)
  return -1 if nums.empty?
  nums[nums.length / 2]
end
