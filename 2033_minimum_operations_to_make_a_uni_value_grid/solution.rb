# LeetCode 2033 - Minimum Operations to Make a Uni-Value Grid
# https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/

# @param {Integer[][]} grid
# @param {Integer} x
# @return {Integer}
def min_operations(grid, x)
  vals = []
  bas = grid[0][0] % x
  grid.each do |row|
    row.each do |v|
      return -1 if v % x != bas

      vals << v
    end
  end
  vals.sort!
  median = vals[vals.length / 2]
  vals.sum { |v| (v - median).abs / x }
end
