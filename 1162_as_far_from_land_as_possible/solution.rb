# LeetCode 1162 - As Far from Land as Possible
# https://leetcode.com/problems/as-far-from-land-as-possible/

# @param {Integer[][]} grid
# @return {Integer}
def max_distance(grid)
  n = grid.length
  queue = []
  n.times { |r| n.times { |c| queue << [r, c] if grid[r][c] == 1 } }
  return -1 if queue.empty? || queue.length == n * n
  dist = -1
  until queue.empty?
    dist += 1
    queue.length.times do
      r, c = queue.shift
      [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]].each do |nr, nc|
        next if nr < 0 || nr >= n || nc < 0 || nc >= n || grid[nr][nc] != 0
        grid[nr][nc] = 1
        queue << [nr, nc]
      end
    end
  end
  dist
end
