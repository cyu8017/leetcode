# LeetCode 3195 - Find the Minimum Area to Cover All Ones I
# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/

# @param {Integer[][]} grid
# @return {Integer}
def minimum_area(grid)
  x1 = grid.length
  y1 = grid[0].length
  x2 = y2 = 0
  grid.each_with_index do |row, i|
    row.each_with_index do |v, j|
      next if v != 1
      x1 = [x1, i].min
      y1 = [y1, j].min
      x2 = [x2, i].max
      y2 = [y2, j].max
    end
  end
  (x2 - x1 + 1) * (y2 - y1 + 1)
end
