# LeetCode 0979 - Distribute Coins in Binary Tree
# https://leetcode.com/problems/distribute-coins-in-binary-tree/

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
def distribute_coins(root)
  ans = [0]
  dfs = lambda do |node|
    return 0 if node.nil?

    left = dfs.call(node.left)
    right = dfs.call(node.right)
    ans[0] += left.abs + right.abs
    node.val + left + right - 1
  end
  dfs.call(root)
  ans[0]
end
