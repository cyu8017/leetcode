# LeetCode 3879 - Maximum Distinct Path Sum in a Binary Tree
# https://leetcode.com/problems/maximum-distinct-path-sum-in-a-binary-tree/

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
def max_sum(root)
  g = {}
  vis = {}
  dfs = nil
  dfs = lambda do |node, p|
    return if node.nil?
    g[node] = [p, node.left, node.right]
    dfs.call(node.left, node)
    dfs.call(node.right, node)
  end
  dfs2 = nil
  dfs2 = lambda do |node|
    return 0 if node.nil? || vis[node.val] == true
    vis[node.val] = true
    res = node.val
    best = 0
    g[node].each { |nxt| best = [best, dfs2.call(nxt)].max }
    vis[node.val] = false
    res + best
  end
  g.clear
  vis.clear
  dfs.call(root, nil)
  ans = -Float::INFINITY
  g.each_key do |node|
    ans = [ans, dfs2.call(node)].max
    vis.clear
  end
  ans.to_i
end
