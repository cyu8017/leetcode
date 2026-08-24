# LeetCode 3970 - Shortest Path With At Most K Consecutive Identical Characters
# https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {String} labels
# @param {Integer} k
# @return {Integer}
def shortest_path(n, edges, labels, k)
  graph = Array.new(n) { [] }
  edges.each { |edge| graph[edge[0]] << [edge[1], edge[2]] }
  infinity = (1 << 53) / 4
  distances = Array.new(n) { Array.new(k + 1, infinity) }
  distances[0][1] = 0
  pq = [[0, 0, 1]]
  until pq.empty?
    pq.sort_by! { |a| a[0] }
    distance, node, run = pq.shift
    next if distance != distances[node][run]
    return distance if node == n - 1
    graph[node].each do |to, weight|
      next_run = labels[node] == labels[to] ? run + 1 : 1
      next if next_run > k
      next_distance = distance + weight
      if next_distance < distances[to][next_run]
        distances[to][next_run] = next_distance
        pq << [next_distance, to, next_run]
      end
    end
  end
  -1
end
