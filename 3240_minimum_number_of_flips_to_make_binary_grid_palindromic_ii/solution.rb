# LeetCode 3240 - Minimum Number of Flips to Make Binary Grid Palindromic II
# https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-ii/

# @param {Integer[][]} grid
# @return {Integer}
def min_flips(grid)
  m = grid.length
  n = grid[0].length
  ans = 0
  (0...(m / 2)).each do |i|
    (0...(n / 2)).each do |j|
      x = m - i - 1
      y = n - j - 1
      cnt1 = grid[i][j] + grid[x][j] + grid[i][y] + grid[x][y]
      ans += [cnt1, 4 - cnt1].min
    end
  end
  ans += grid[m / 2][n / 2] if m.odd? && n.odd?
  diff = 0
  ones = 0
  if m.odd?
    (0...(n / 2)).each do |j|
      if grid[m / 2][j] == grid[m / 2][n - j - 1]
        ones += grid[m / 2][j] * 2
      else
        diff += 1
      end
    end
  end
  if n.odd?
    (0...(m / 2)).each do |i|
      if grid[i][n / 2] == grid[m - i - 1][n / 2]
        ones += grid[i][n / 2] * 2
      else
        diff += 1
      end
    end
  end
  if ones % 4 == 0 || diff > 0
    ans += diff
  else
    ans += 2
  end
  ans
end
