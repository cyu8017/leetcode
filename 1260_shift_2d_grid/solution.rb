# LeetCode 1260 - Shift 2D Grid
# https://leetcode.com/problems/shift-2d-grid/

# @param {Integer[][]} grid
# @param {Integer} k
# @return {Integer[][]}
def shift_grid(grid, k)
  m = grid.length
  n = grid[0].length
  flat = grid.flatten
  k %= flat.length
  flat = flat[-k..] + flat[0...-k] if k > 0
  Array.new(m) { |i| flat[i * n...(i + 1) * n] }
end
