# LeetCode 2906 - Construct Product Matrix
# https://leetcode.com/problems/construct-product-matrix/

# @param {Integer[][]} grid
# @return {Integer[][]}
def construct_product_matrix(grid)
  mod = 12345
  m = grid.length
  n = grid[0].length
  ans = Array.new(m) { Array.new(n, 0) }
  pref = 1
  (0...m).each do |i|
    (0...n).each do |j|
      ans[i][j] = pref
      pref = (pref * (grid[i][j] % mod)) % mod
    end
  end
  suf = 1
  (m - 1).downto(0) do |i|
    (n - 1).downto(0) do |j|
      ans[i][j] = (ans[i][j] * suf) % mod
      suf = (suf * (grid[i][j] % mod)) % mod
    end
  end
  ans
end
