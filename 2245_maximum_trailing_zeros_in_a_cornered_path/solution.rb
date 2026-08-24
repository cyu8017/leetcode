# LeetCode 2245 - Maximum Trailing Zeros in a Cornered Path
# https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/

# @param {Integer[][]} grid
# @return {Integer}
def max_trailing_zeros(grid)
  fact = lambda do |x|
    t = f = 0
    while x.even?
      t += 1
      x /= 2
    end
    while x % 5 == 0
      f += 1
      x /= 5
    end
    [t, f]
  end

  m = grid.length
  n = grid[0].length
  left2 = Array.new(m) { Array.new(n, 0) }
  left5 = Array.new(m) { Array.new(n, 0) }
  up2 = Array.new(m) { Array.new(n, 0) }
  up5 = Array.new(m) { Array.new(n, 0) }
  m.times do |i|
    n.times do |j|
      p0, p1 = fact.call(grid[i][j])
      left2[i][j] = up2[i][j] = p0
      left5[i][j] = up5[i][j] = p1
      if j > 0
        left2[i][j] += left2[i][j - 1]
        left5[i][j] += left5[i][j - 1]
      end
      if i > 0
        up2[i][j] += up2[i - 1][j]
        up5[i][j] += up5[i - 1][j]
      end
    end
  end
  ans = 0
  m.times do |i|
    n.times do |j|
      cell = fact.call(grid[i][j])
      l2 = left2[i][j]
      l5 = left5[i][j]
      r2 = left2[i][n - 1] - left2[i][j] + cell[0]
      r5 = left5[i][n - 1] - left5[i][j] + cell[1]
      u2 = up2[i][j]
      u5 = up5[i][j]
      d2 = up2[m - 1][j] - up2[i][j] + cell[0]
      d5 = up5[m - 1][j] - up5[i][j] + cell[1]
      [
        [l2 + u2 - cell[0], l5 + u5 - cell[1]],
        [l2 + d2 - cell[0], l5 + d5 - cell[1]],
        [r2 + u2 - cell[0], r5 + u5 - cell[1]],
        [r2 + d2 - cell[0], r5 + d5 - cell[1]]
      ].each { |a, b| ans = [ans, [a, b].min].max }
    end
  end
  ans
end
