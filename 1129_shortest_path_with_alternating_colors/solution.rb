# LeetCode 1129 - Shortest Path with Alternating Colors
# https://leetcode.com/problems/shortest-path-with-alternating-colors/

# @param {Integer} n
# @param {Integer[][]} red_edges
# @param {Integer[][]} blue_edges
# @return {Integer[]}
def shortest_alternating_paths(n, red_edges, blue_edges)
  red = Array.new(n) { [] }
  blue = Array.new(n) { [] }
  red_edges.each { |a, b| red[a] << b }
  blue_edges.each { |a, b| blue[a] << b }
  ans = Array.new(n, -1)
  ans[0] = 0
  # queue: [node, color] color 0=red, 1=blue
  queue = [[0, 0], [0, 1]]
  visited = Array.new(n) { [false, false] }
  visited[0][0] = visited[0][1] = true
  dist = 0
  until queue.empty?
    dist += 1
    queue.length.times do
      node, color = queue.shift
      edges = color == 0 ? red[node] : blue[node]
      edges.each do |nxt|
        next_color = 1 - color
        next if visited[nxt][next_color]
        visited[nxt][next_color] = true
        ans[nxt] = dist if ans[nxt] == -1
        queue << [nxt, next_color]
      end
    end
  end
  ans
end
