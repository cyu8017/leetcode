# LeetCode 0807 - Max Increase to Keep City Skyline
# https://leetcode.com/problems/max-increase-to-keep-city-skyline/

# @param {Integer[][]} grid
# @return {Integer}
def max_increase_keeping_skyline(grid)
  row_max = grid.map(&:max)
  col_max = grid.transpose.map(&:max)
  grid.each_with_index.sum do |row, r|
    row.each_with_index.sum { |h, c| [row_max[r], col_max[c]].min - h }
  end
end
