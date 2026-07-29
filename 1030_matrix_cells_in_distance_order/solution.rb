# LeetCode 1030 - Matrix Cells in Distance Order
# https://leetcode.com/problems/matrix-cells-in-distance-order/

# @param {Integer} rows
# @param {Integer} cols
# @param {Integer} r_center
# @param {Integer} c_center
# @return {Integer[][]}
def all_cells_dist_order(rows, cols, r_center, c_center)
  cells = []
  rows.times { |r| cols.times { |c| cells << [r, c] } }
  cells.sort_by { |r, c| (r - r_center).abs + (c - c_center).abs }
end
