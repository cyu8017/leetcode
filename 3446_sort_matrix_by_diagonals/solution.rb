# LeetCode 3446 - Sort Matrix by Diagonals
# https://leetcode.com/problems/sort-matrix-by-diagonals/

# @param {Integer[][]} grid
# @return {Integer[][]}
def sort_matrix(grid)
  n = grid.length
  diags = {}
  (0...n).each do |i|
    (0...n).each do |j|
      key = i - j
      diags[key] ||= []
      diags[key] << grid[i][j]
    end
  end
  diags.each do |key, lst|
    if key >= 0
      lst.sort! { |a, b| b <=> a }
    else
      lst.sort!
    end
  end
  idx = {}
  (0...n).each do |i|
    (0...n).each do |j|
      k = i - j
      pos = idx[k] || 0
      grid[i][j] = diags[k][pos]
      idx[k] = pos + 1
    end
  end
  grid
end
