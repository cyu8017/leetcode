# LeetCode 2378 - Choose Edges to Maximize Score in a Tree
# https://leetcode.com/problems/choose-edges-to-maximize-score-in-a-tree/

# @param {Integer[][]} edges
# @return {Integer}
def max_score(edges)
  n = edges.length
  g = Array.new(n) { [] }
  (1...n).each do |i|
    p = edges[i][0]
    w = edges[i][1]
    g[p] << [i, w]
  end
  dfs = lambda do |u|
    base = 0
    best_gain = 0
    g[u].each do |to, w|
      child = dfs.call(to)
      base += child[0]
      gain = child[1] + w - child[0]
      best_gain = gain if gain > best_gain
    end
    [base + best_gain, base]
  end
  dfs.call(0)[0]
end

alias solve max_score
