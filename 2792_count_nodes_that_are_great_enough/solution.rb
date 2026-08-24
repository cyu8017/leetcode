# LeetCode 2792 - Count Nodes That Are Great Enough
# https://leetcode.com/problems/count-nodes-that-are-great-enough/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {TreeNode} root
# @param {Integer} k
# @return {Integer}
def count_great_enough_nodes(root, k)
  ans = [0]
  dfs = lambda do |node|
    return [] if node.nil?
    vals = [node.val] + dfs.call(node.left) + dfs.call(node.right)
    smaller = vals.count { |v| v < node.val }
    ans[0] += 1 if smaller >= k
    vals
  end
  dfs.call(root)
  ans[0]
end
