# LeetCode 3910 - Count Connected Subgraphs with Even Node Sum
# https://leetcode.com/problems/count-connected-subgraphs-with-even-node-sum/

# @param {Integer[]} nums
# @param {Integer[][]} edges
# @return {Integer}
def even_sum_subgraphs(nums, edges)
  n = nums.length
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << e[1]
    g[e[1]] << e[0]
  end
  m = (1 << n) - 1
  vis = 0
  dfs = nil
  dfs = lambda do |u|
    vis |= 1 << u
    g[u].each do |v|
      dfs.call(v) if ((vis >> v) & 1) == 0
    end
  end
  ans = 0
  (1..m).each do |sub|
    s = 0
    n.times { |i| s += nums[i] if ((sub >> i) & 1) != 0 }
    next if s.odd?
    vis = m ^ sub
    start = sub.bit_length - 1
    start = 0 if sub == 0
    dfs.call(start)
    ans += 1 if vis == m
  end
  ans
end
