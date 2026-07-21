# LeetCode 1878 - Get Biggest Three Rhombus Sums in a Grid
# https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/

# @param {Integer[][]} grid
# @return {Integer[]}
def get_biggest_three(grid)
  m = grid.length
  n = grid[0].length
  s1 = Array.new(m + 1) { Array.new(n + 2, 0) }
  s2 = Array.new(m + 1) { Array.new(n + 2, 0) }

  grid.each_with_index do |row, ii|
    i = ii + 1
    row.each_with_index do |value, jj|
      j = jj + 1
      s1[i][j] = s1[i - 1][j - 1] + value
      s2[i][j] = s2[i - 1][j + 1] + value
    end
  end

  rhombus_sums = {}
  grid.each_with_index do |row, ii|
    i = ii + 1
    row.each_with_index do |value, jj|
      j = jj + 1
      limit = [i - 1, m - i, j - 1, n - j].min
      rhombus_sums[value] = true
      (1..limit).each do |k|
        a = s1[i + k][j] - s1[i][j - k]
        b = s1[i][j + k] - s1[i - k][j]
        c = s2[i][j - k] - s2[i - k][j]
        d = s2[i + k][j] - s2[i][j + k]
        rhombus_sums[a + b + c + d - grid[i + k - 1][j - 1] + grid[i - k - 1][j - 1]] = true
      end
    end
  end

  rhombus_sums.keys.sort.reverse.take(3)
end
