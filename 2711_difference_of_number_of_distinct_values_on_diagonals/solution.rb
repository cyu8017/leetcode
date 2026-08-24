# LeetCode 2711 - Difference of Number of Distinct Values on Diagonals
# https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/

# @param {Integer[][]} grid
# @return {Integer[][]}
def difference_of_distinct_values(grid)
  m = grid.length
  n = grid[0].length
  ans = Array.new(m) { Array.new(n, 0) }
  m.times do |i|
    n.times do |j|
      top = {}
      bot = {}
      r = i - 1
      c = j - 1
      while r >= 0 && c >= 0
        top[grid[r][c]] = true
        r -= 1
        c -= 1
      end
      r = i + 1
      c = j + 1
      while r < m && c < n
        bot[grid[r][c]] = true
        r += 1
        c += 1
      end
      ans[i][j] = (top.length - bot.length).abs
    end
  end
  ans
end
