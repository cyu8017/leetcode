# LeetCode 3067 - Count Pairs of Connectable Servers in a Weighted Tree Network
# https://leetcode.com/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/

# @param {Integer[][]} edges
# @param {Integer} signal_speed
# @return {Integer[]}
def count_pairs_of_connectable_servers(edges, signal_speed)
  n = edges.length + 1
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << [e[1], e[2]]
    g[e[1]] << [e[0], e[2]]
  end

  dfs = lambda do |a, fa, ws|
    cnt = ws % signal_speed == 0 ? 1 : 0
    g[a].each do |b, w|
      cnt += dfs.call(b, a, ws + w) if b != fa
    end
    cnt
  end

  ans = Array.new(n, 0)
  n.times do |a|
    s = 0
    g[a].each do |b, w|
      t = dfs.call(b, a, w)
      ans[a] += s * t
      s += t
    end
  end
  ans
end
