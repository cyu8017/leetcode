# LeetCode 2146 - K Highest Ranked Items Within a Price Range
# https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range/

# @param {Integer[][]} grid
# @param {Integer[]} pricing
# @param {Integer[]} start
# @param {Integer} k
# @return {Integer[][]}
def highest_ranked_k_items(grid, pricing, start, k)
  m = grid.length
  n = grid[0].length
  low, high = pricing
  vis = Array.new(m) { Array.new(n, false) }
  q = [[start[0], start[1], 0]]
  vis[start[0]][start[1]] = true
  cands = []
  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  until q.empty?
    r, c, d = q.shift
    cands << [d, grid[r][c], r, c] if grid[r][c] >= low && grid[r][c] <= high
    dirs.each do |dr, dc|
      nr = r + dr
      nc = c + dc
      if nr >= 0 && nr < m && nc >= 0 && nc < n && !vis[nr][nc] && grid[nr][nc] != 0
        vis[nr][nc] = true
        q << [nr, nc, d + 1]
      end
    end
  end
  cands.sort!
  k = cands.length if k > cands.length
  (0...k).map { |i| [cands[i][2], cands[i][3]] }
end
