# LeetCode 1617 - Count Subtrees With Max Distance Between Cities
# https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer[]}
def count_subgraphs_for_each_diameter(n, edges)
  adj = Array.new(n) { [] }
  edges.each do |a, b|
    a -= 1
    b -= 1
    adj[a] << b
    adj[b] << a
  end
  ans = Array.new(n - 1, 0)
  (1...(1 << n)).each do |mask|
    next if (mask & (mask - 1)).zero?

    start = Math.log2(mask & -mask).to_i
    bfs = lambda do |src|
      dist = { src => 0 }
      q = [src]
      q.each do |u|
        adj[u].each do |v|
          next unless (mask >> v & 1) == 1 && !dist.key?(v)

          dist[v] = dist[u] + 1
          q << v
        end
      end
      far = dist.max_by { |_, d| d }[0]
      [far, dist]
    end
    far, seen = bfs.call(start)
    next unless seen.length == mask.to_s(2).count("1")

    _, dist = bfs.call(far)
    ans[dist.values.max - 1] += 1
  end
  ans
end
