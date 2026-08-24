# LeetCode 3243 - Shortest Distance After Road Addition Queries I
# https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/

# @param {Integer} n
# @param {Integer[][]} queries
# @return {Integer[]}
def shortest_distance_after_queries(n, queries)
  g = Array.new(n) { [] }
  (0...n - 1).each { |i| g[i] << i + 1 }
  bfs = lambda do
    q = [0]
    vis = Array.new(n, false)
    vis[0] = true
    d = 0
    loop do
      k = q.length
      while k > 0
        u = q.shift
        return d if u == n - 1
        g[u].each do |v|
          unless vis[v]
            vis[v] = true
            q << v
          end
        end
        k -= 1
      end
      d += 1
    end
  end
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, i|
    g[q[0]] << q[1]
    ans[i] = bfs.call
  end
  ans
end
