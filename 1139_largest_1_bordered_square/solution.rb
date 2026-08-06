# LeetCode 1139 - Largest 1-Bordered Square
# https://leetcode.com/problems/largest-1-bordered-square/

# @param {Integer[][]} grid
# @return {Integer}
def largest1_bordered_square(grid)
  m = grid.length
  n = grid[0].length
  left = Array.new(m) { Array.new(n, 0) }
  up = Array.new(m) { Array.new(n, 0) }
  m.times do |r|
    n.times do |c|
      next if grid[r][c].zero?
      left[r][c] = 1 + (c > 0 ? left[r][c - 1] : 0)
      up[r][c] = 1 + (r > 0 ? up[r - 1][c] : 0)
    end
  end
  best = 0
  m.times do |r|
    n.times do |c|
      next if grid[r][c].zero?
      limit = [left[r][c], up[r][c]].min
      limit.downto(1) do |size|
        if left[r - size + 1][c] >= size && up[r][c - size + 1] >= size
          best = [best, size].max
          break
        end
      end
    end
  end
  best * best
end
