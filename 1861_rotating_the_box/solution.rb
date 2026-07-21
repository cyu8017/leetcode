# LeetCode 1861 - Rotating the Box
# https://leetcode.com/problems/rotating-the-box/

# @param {Character[][]} box_grid
# @return {Character[][]}
def rotate_the_box(box_grid)
  m = box_grid.length
  n = box_grid[0].length
  rotated = Array.new(n) { Array.new(m, ".") }

  (0...n).each do |i|
    (0...m).each do |j|
      rotated[i][j] = box_grid[m - 1 - j][i]
    end
  end

  (0...m).each do |col|
    row = n - 1
    (n - 1).downto(0) do |i|
      if rotated[i][col] == "*"
        row = i - 1
      elsif rotated[i][col] == "#"
        rotated[i][col] = "."
        rotated[row][col] = "#"
        row -= 1
      end
    end
  end

  rotated
end
