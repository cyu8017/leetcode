# LeetCode 2065 - Maximum Path Quality of a Graph
# https://leetcode.com/problems/maximum-path-quality-of-a-graph/

# @param {Integer[]} values
# @param {Integer[][]} edges
# @param {Integer} max_time
# @return {Integer}
def maximal_path_quality(values, edges, max_time)
  n = values.length
  g = Array.new(n) { [] }
  edges.each do |u, v, t|
    g[u] << [v, t]
    g[v] << [u, t]
  end
  ans = 0
  vis = Array.new(n, 0)
  dfs = lambda do |u, time, quality|
    return if time > max_time

    first = vis[u].zero?
    quality += values[u] if first
    vis[u] += 1
    ans = [ans, quality].max if u.zero?
    g[u].each { |v, w| dfs.call(v, time + w, quality) }
    vis[u] -= 1
  end
  dfs.call(0, 0, 0)
  ans
end
