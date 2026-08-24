# LeetCode 3997 - Count Dominant Nodes in a Binary Tree
# https://leetcode.com/problems/count-dominant-nodes-in-a-binary-tree/

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
def count_dominant_nodes(root)
  ans = 0
  dfs = nil
  dfs = lambda do |node|
    return -2_147_483_648 if node.nil?
    l = dfs.call(node.left)
    r = dfs.call(node.right)
    mx = [l, r, node.val].max
    ans += 1 if mx == node.val
    mx
  end
  dfs.call(root)
  ans
end
