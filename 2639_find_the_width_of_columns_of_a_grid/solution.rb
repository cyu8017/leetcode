# LeetCode 2639 - Find the Width of Columns of a Grid
# https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/

# @param {Integer[][]} grid
# @return {Integer[]}
def find_column_width(grid)
  n = grid[0].length
  ans = Array.new(n, 0)
  width = lambda do |x|
    return 1 if x == 0

    w = 0
    if x < 0
      w += 1
      x = -x
    end
    while x > 0
      w += 1
      x /= 10
    end
    w
  end
  grid.each do |row|
    n.times { |j| ans[j] = [ans[j], width.call(row[j])].max }
  end
  ans
end
