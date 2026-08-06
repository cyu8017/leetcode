# LeetCode 1102 - Path With Maximum Minimum Value
# https://leetcode.com/problems/path-with-maximum-minimum-value/

# @param {Integer[][]} grid
# @return {Integer}
def maximum_minimum_path(grid)
  require "set"
  m = grid.length
  n = grid[0].length
  # max-heap via negated values in a sorted insert (small grids) — use array + sort
  heap = [[-grid[0][0], 0, 0]]
  seen = Set[[0, 0]]
  until heap.empty?
    heap.sort_by! { |v, _, _| v }
    val, r, c = heap.shift
    return -val if r == m - 1 && c == n - 1
    [[1, 0], [-1, 0], [0, 1], [0, -1]].each do |dr, dc|
      nr = r + dr
      nc = c + dc
      next if nr < 0 || nr >= m || nc < 0 || nc >= n
      next if seen.include?([nr, nc])
      seen.add([nr, nc])
      heap << [[val, -grid[nr][nc]].max, nr, nc]
    end
  end
  grid[0][0]
end
