# LeetCode 2415 - Reverse Odd Levels of Binary Tree
# https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @return {TreeNode}
def reverse_odd_levels(root)
  dfs = lambda do |a, b, level|
    return if a.nil? || b.nil?
    a.val, b.val = b.val, a.val if level.odd?
    dfs.call(a.left, b.right, level + 1)
    dfs.call(a.right, b.left, level + 1)
  end
  dfs.call(root.left, root.right, 1) unless root.nil?
  root
end
