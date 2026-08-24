# LeetCode 3812 - Minimum Edge Toggles on a Tree
# https://leetcode.com/problems/minimum-edge-toggles-on-a-tree/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[]} start
# @param {Integer[]} target
# @return {Integer[]}
def minimum_flips(n, edges, start, target)
  g = Array.new(n) { [] }
  (0...(n - 1)).each do |i|
    a = edges[i][0]
    b = edges[i][1]
    g[a] << [b, i]
    g[b] << [a, i]
  end
  ans = []
  dfs = nil
  dfs = lambda do |a, fa|
    rev = start[a] != target[a]
    g[a].each do |b, i|
      if b != fa && dfs.call(b, a)
        ans << i
        rev = !rev
      end
    end
    rev
  end
  return [-1] if dfs.call(0, -1)
  ans.sort
end
