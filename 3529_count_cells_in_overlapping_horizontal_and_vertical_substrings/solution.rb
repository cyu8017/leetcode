# LeetCode 3529 - Count Cells in Overlapping Horizontal and Vertical Substrings
# https://leetcode.com/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings/

# @param {String[][]} grid
# @param {String} pattern
# @return {Integer}
def count_cells(grid, pattern)
  m = grid.length
  n = grid[0].length
  row = ""
  (0...m).each { |i| (0...n).each { |j| row += grid[i][j] } }
  col = ""
  (0...n).each { |j| (0...m).each { |i| col += grid[i][j] } }
  h_mark = Array.new(m) { Array.new(n, false) }
  v_mark = Array.new(m) { Array.new(n, false) }
  plen = pattern.length
  (0..(row.length - plen)).each do |i|
    next unless row[i, plen] == pattern
    (0...plen).each do |t|
      pos = i + t
      h_mark[pos / n][pos % n] = true
    end
  end
  (0..(col.length - plen)).each do |i|
    next unless col[i, plen] == pattern
    (0...plen).each do |t|
      pos = i + t
      v_mark[pos % m][pos / m] = true
    end
  end
  ans = 0
  (0...m).each do |i|
    (0...n).each { |j| ans += 1 if h_mark[i][j] && v_mark[i][j] }
  end
  ans
end
