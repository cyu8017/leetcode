# LeetCode 1267 - Count Servers that Communicate
# https://leetcode.com/problems/count-servers-that-communicate/

# @param {Integer[][]} grid
# @return {Integer}
def count_servers(grid)
  rows = grid.map(&:sum)
  cols = grid[0].length.times.map { |c| grid.sum { |row| row[c] } }
  ans = 0
  grid.each_with_index do |row, r|
    row.each_with_index do |cell, c|
      ans += 1 if cell == 1 && (rows[r] > 1 || cols[c] > 1)
    end
  end
  ans
end
