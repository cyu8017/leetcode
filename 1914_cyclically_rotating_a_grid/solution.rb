# LeetCode 1914 - Cyclically Rotating a Grid
# https://leetcode.com/problems/cyclically-rotating-a-grid/

# @param {Integer[][]} grid
# @param {Integer} k
# @return {Integer[][]}
def rotate_grid(grid, k)
  m = grid.length
  n = grid[0].length
  layers = [m, n].min / 2
  layers.times do |layer|
    vals = []
    (layer...n - layer).each { |c| vals << grid[layer][c] }
    (layer + 1...m - layer).each { |r| vals << grid[r][n - layer - 1] }
    if m - 2 * layer > 1
      (n - layer - 2).downto(layer) { |c| vals << grid[m - layer - 1][c] }
    end
    if n - 2 * layer > 1
      (m - layer - 2).downto(layer + 1) { |r| vals << grid[r][layer] }
    end
    shift = k % vals.length
    rotated = vals[shift..] + vals[0...shift]
    idx = 0
    (layer...n - layer).each do |c|
      grid[layer][c] = rotated[idx]
      idx += 1
    end
    (layer + 1...m - layer).each do |r|
      grid[r][n - layer - 1] = rotated[idx]
      idx += 1
    end
    if m - 2 * layer > 1
      (n - layer - 2).downto(layer) do |c|
        grid[m - layer - 1][c] = rotated[idx]
        idx += 1
      end
    end
    if n - 2 * layer > 1
      (m - layer - 2).downto(layer + 1) do |r|
        grid[r][layer] = rotated[idx]
        idx += 1
      end
    end
  end
  grid
end
