# LeetCode 3241 - Time Taken to Mark All Nodes
# https://leetcode.com/problems/time-taken-to-mark-all-nodes/

# @param {Integer[][]} edges
# @return {Integer[]}
def time_taken(edges)
  n = edges.length + 1
  ans = Array.new(n, 0)
  tree = Array.new(n) { [] }
  dp = Array.new(n) { { top1: { node: 0, time: 0 }, top2: { node: 0, time: 0 } } }
  edges.each do |e|
    tree[e[0]] << e[1]
    tree[e[1]] << e[0]
  end
  get_time = lambda { |u| u.even? ? 2 : 1 }
  dfs = nil
  dfs = lambda do |u, prev|
    t1 = { node: 0, time: 0 }
    t2 = { node: 0, time: 0 }
    tree[u].each do |v|
      next if v == prev
      t = dfs.call(v, u) + get_time.call(v)
      if t >= t1[:time]
        t2 = t1
        t1 = { node: v, time: t }
      elsif t > t2[:time]
        t2 = { node: v, time: t }
      end
    end
    dp[u][:top1] = t1
    dp[u][:top2] = t2
    t1[:time]
  end
  reroot = nil
  reroot = lambda do |u, prev, max_time|
    ans[u] = max_time
    ans[u] = dp[u][:top1][:time] if dp[u][:top1][:time] > ans[u]
    tree[u].each do |v|
      next if v == prev
      side = dp[u][:top1][:node] == v ? dp[u][:top2][:time] : dp[u][:top1][:time]
      reroot.call(v, u, get_time.call(u) + [max_time, side].max)
    end
  end
  dfs.call(0, -1)
  reroot.call(0, -1, 0)
  ans
end
