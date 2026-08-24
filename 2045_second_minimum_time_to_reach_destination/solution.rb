# LeetCode 2045 - Second Minimum Time to Reach Destination
# https://leetcode.com/problems/second-minimum-time-to-reach-destination/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer} time
# @param {Integer} change
# @return {Integer}
def second_minimum(n, edges, time, change)
  g = Array.new(n + 1) { [] }
  edges.each do |u, v|
    g[u] << v
    g[v] << u
  end
  dist1 = Array.new(n + 1, -1)
  dist2 = Array.new(n + 1, -1)
  q = [[1, 0]]
  dist1[1] = 0
  until q.empty?
    u, d = q.shift
    g[u].each do |v|
      nd = d + 1
      if dist1[v] == -1
        dist1[v] = nd
        q << [v, nd]
      elsif dist2[v] == -1 && nd > dist1[v]
        dist2[v] = nd
        q << [v, nd]
      end
    end
  end
  steps = dist2[n]
  ans = 0
  steps.times do
    ans += change - ans % change if (ans / change).odd?
    ans += time
  end
  ans
end
