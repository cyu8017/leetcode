# LeetCode 2050 - Parallel Courses III
# https://leetcode.com/problems/parallel-courses-iii/

# @param {Integer} n
# @param {Integer[][]} relations
# @param {Integer[]} time
# @return {Integer}
def minimum_time(n, relations, time)
  g = Array.new(n + 1) { [] }
  indeg = Array.new(n + 1, 0)
  dist = Array.new(n + 1, 0)
  relations.each do |u, v|
    g[u] << v
    indeg[v] += 1
  end
  q = []
  (1..n).each do |i|
    dist[i] = time[i - 1]
    q << i if indeg[i].zero?
  end
  until q.empty?
    u = q.shift
    g[u].each do |v|
      dist[v] = [dist[v], dist[u] + time[v - 1]].max
      indeg[v] -= 1
      q << v if indeg[v].zero?
    end
  end
  dist[1..].max
end
