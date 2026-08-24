# LeetCode 3619 - Count Islands With Total Value Divisible by K
# https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/

# @param {Integer[][]} grid
# @param {Integer} k
# @return {Integer}
def count_islands(grid, k)
  m = grid.length
  n = grid[0].length
  dirs = [-1, 0, 1, 0, -1]
  dfs = nil
  dfs = lambda do |i, j|
    s = grid[i][j]
    grid[i][j] = 0
    4.times do |d|
      x = i + dirs[d]
      y = j + dirs[d + 1]
      s += dfs.call(x, y) if x >= 0 && x < m && y >= 0 && y < n && grid[x][y] > 0
    end
    s
  end
  ans = 0
  (0...m).each do |i|
    (0...n).each do |j|
      ans += 1 if grid[i][j] > 0 && dfs.call(i, j) % k == 0
    end
  end
  ans
end
