# LeetCode 1377 - Frog Position After T Seconds
# https://leetcode.com/problems/frog-position-after-t-seconds/

def frog_position(n, edges, t, target)
  g = Array.new(n + 1) { [] }
  edges.each do |a, b|
    g[a] << b
    g[b] << a
  end
  dfs = lambda do |u, p, time, prob|
    kids = g[u].reject { |v| v == p }
    return (u == target ? prob : 0) if time == t || kids.empty?
    kids.sum { |v| dfs.call(v, u, time + 1, prob / kids.length.to_f) }
  end
  dfs.call(1, 0, 0, 1.0)
end
