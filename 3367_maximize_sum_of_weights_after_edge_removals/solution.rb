# LeetCode 3367 - Maximize Sum of Weights after Edge Removals
# https://leetcode.com/problems/maximize-sum-of-weights-after-edge-removals/

# @param {Integer[][]} edges
# @param {Integer} k
# @return {Integer}
def maximize_sum_of_weights(edges, k)
  n = edges.length + 1
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << [e[1], e[2]]
    g[e[1]] << [e[0], e[2]]
  end
  dfs = lambda do |u, p|
    base = 0
    gains = []
    g[u].each do |to, w|
      next if to == p

      child = dfs.call(to, u)
      base += child[1]
      gain = child[0] + w - child[1]
      gains << gain if gain > 0
    end
    gains.sort!.reverse!
    with_p = base
    without = base
    [gains.length, k - 1].min.times { |i| with_p += gains[i] }
    [gains.length, k].min.times { |i| without += gains[i] }
    [with_p, without]
  end
  dfs.call(0, -1)[1]
end
