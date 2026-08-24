# LeetCode 3311 - Construct 2D Grid Matching Graph Layout
# https://leetcode.com/problems/construct-2d-grid-matching-graph-layout/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer[][]}
def construct_grid_layout(n, edges)
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << e[1]
    g[e[1]] << e[0]
  end
  deg = n.times.map { |i| g[i].length }
  start = 0
  n.times do |i|
    if deg[i] == 1
      start = i
      break
    end
    start = i if deg[i] == 2
  end
  vis = Array.new(n, false)
  row = []
  cur = start
  prev = -1
  loop do
    row << cur
    vis[cur] = true
    nxt = -1
    g[cur].each do |v|
      next unless v != prev && !vis[v] && deg[v] <= 3

      nxt = v
      break if deg[v] < 4
    end
    break if nxt == -1

    prev = cur
    cur = nxt
  end
  width = row.length
  height = width != 0 ? n / width : n
  if width == 0 || width * height != n
    (1..n).each do |w|
      next unless n % w == 0

      width = w
      height = n / w
      break
    end
  end
  grid = Array.new(height) { Array.new(width, 0) }
  n.times { |i| grid[i / width][i % width] = i }
  grid
end
