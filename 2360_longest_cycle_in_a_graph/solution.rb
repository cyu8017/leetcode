# LeetCode 2360 - Longest Cycle in a Graph
# https://leetcode.com/problems/longest-cycle-in-a-graph/

# @param {Integer[]} edges
# @return {Integer}
def longest_cycle(edges)
  n = edges.length
  vis = Array.new(n, false)
  ans = -1
  (0...n).each do |i|
    next if vis[i]
    dist = {}
    cur = i
    step = 0
    while cur != -1 && !vis[cur]
      vis[cur] = true
      dist[cur] = step
      cur = edges[cur]
      step += 1
    end
    if cur != -1 && dist.key?(cur)
      cand = step - dist[cur]
      ans = cand if cand > ans
    end
  end
  ans
end
