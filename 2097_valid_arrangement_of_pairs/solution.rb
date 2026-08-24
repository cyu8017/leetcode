# LeetCode 2097 - Valid Arrangement of Pairs
# https://leetcode.com/problems/valid-arrangement-of-pairs/

# @param {Integer[][]} pairs
# @return {Integer[][]}
def valid_arrangement(pairs)
  g = Hash.new { |h, k| h[k] = [] }
  indeg = Hash.new(0)
  outdeg = Hash.new(0)
  pairs.each do |u, v|
    g[u] << v
    outdeg[u] += 1
    indeg[v] += 1
  end
  start = pairs[0][0]
  outdeg.each do |u, o|
    if o - indeg[u] == 1
      start = u
      break
    end
  end
  path = []
  dfs = lambda do |u|
    nbrs = g[u]
    dfs.call(nbrs.pop) until nbrs.empty?
    path << u
  end
  dfs.call(start)
  path.reverse!
  (0...path.length - 1).map { |i| [path[i], path[i + 1]] }
end
