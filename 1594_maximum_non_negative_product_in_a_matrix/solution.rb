# LeetCode 1594 - Maximum Non Negative Product in a Matrix
# https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/

# @param {Integer[][]} grid
# @return {Integer}
def max_product_path(grid)
  mod = 1_000_000_007
  m = grid.length
  n = grid[0].length
  high = Array.new(m) { Array.new(n, 0) }
  low = Array.new(m) { Array.new(n, 0) }
  high[0][0] = low[0][0] = grid[0][0]
  (0...m).each do |r|
    (0...n).each do |c|
      next if r.zero? && c.zero?
      values = []
      if r.positive?
        values << high[r - 1][c] * grid[r][c]
        values << low[r - 1][c] * grid[r][c]
      end
      if c.positive?
        values << high[r][c - 1] * grid[r][c]
        values << low[r][c - 1] * grid[r][c]
      end
      high[r][c] = values.max
      low[r][c] = values.min
    end
  end
  high[-1][-1] >= 0 ? high[-1][-1] % mod : -1
end
