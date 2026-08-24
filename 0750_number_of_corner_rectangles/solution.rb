# LeetCode 0750 - Number Of Corner Rectangles
# https://leetcode.com/problems/number-of-corner-rectangles/

# @param {Integer[][]} grid
# @return {Integer}
def count_corner_rectangles(grid)
  m = grid.length
  n = grid[0].length
  ans = 0
  m.times do |i|
    ((i + 1)...m).each do |j|
      count = 0
      n.times { |c| count += 1 if grid[i][c] != 0 && grid[j][c] != 0 }
      ans += count * (count - 1) / 2
    end
  end
  ans
end
