# LeetCode 3197 - Find the Minimum Area to Cover All Ones II
# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/

# @param {Integer[][]} grid
# @return {Integer}
def minimum_sum(grid)
  m = grid.length
  n = grid[0].length
  ans = m * n
  area = lambda do |i1, j1, i2, j2|
    inf = 10**18
    x1 = y1 = inf
    x2 = y2 = -inf
    (i1..i2).each do |i|
      (j1..j2).each do |j|
        next if grid[i][j] != 1
        x1 = [x1, i].min
        y1 = [y1, j].min
        x2 = [x2, i].max
        y2 = [y2, j].max
      end
    end
    return 0 if x1 == inf
    (x2 - x1 + 1) * (y2 - y1 + 1)
  end
  (0...m - 1).each do |i1|
    ((i1 + 1)...m - 1).each do |i2|
      ans = [
        ans,
        area.call(0, 0, i1, n - 1) + area.call(i1 + 1, 0, i2, n - 1) + area.call(i2 + 1, 0, m - 1, n - 1)
      ].min
    end
  end
  (0...n - 1).each do |j1|
    ((j1 + 1)...n - 1).each do |j2|
      ans = [
        ans,
        area.call(0, 0, m - 1, j1) + area.call(0, j1 + 1, m - 1, j2) + area.call(0, j2 + 1, m - 1, n - 1)
      ].min
    end
  end
  (0...m - 1).each do |i|
    (0...n - 1).each do |j|
      ans = [ans, area.call(0, 0, i, j) + area.call(0, j + 1, i, n - 1) + area.call(i + 1, 0, m - 1, n - 1)].min
      ans = [ans, area.call(0, 0, i, n - 1) + area.call(i + 1, 0, m - 1, j) + area.call(i + 1, j + 1, m - 1, n - 1)].min
      ans = [ans, area.call(0, 0, i, j) + area.call(i + 1, 0, m - 1, j) + area.call(0, j + 1, m - 1, n - 1)].min
      ans = [ans, area.call(0, 0, m - 1, j) + area.call(0, j + 1, i, n - 1) + area.call(i + 1, j + 1, m - 1, n - 1)].min
    end
  end
  ans
end
