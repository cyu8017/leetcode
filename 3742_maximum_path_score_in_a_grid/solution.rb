# LeetCode 3742 - Maximum Path Score in a Grid
# https://leetcode.com/problems/maximum-path-score-in-a-grid/

# @param {Integer[][]} grid
# @param {Integer} k
# @return {Integer}
def max_path_score(grid, k)
  inf = 1 << 30
  m = grid.length
  n = grid[0].length
  f = Array.new(m) { Array.new(n) { Array.new(k + 1, -1) } }
  dfs = nil
  dfs = lambda do |i, j, kk|
    return -inf if i < 0 || j < 0 || kk < 0
    return 0 if i == 0 && j == 0
    return f[i][j][kk] if f[i][j][kk] != -1
    res = grid[i][j]
    nk = kk
    nk -= 1 if grid[i][j] != 0
    a = dfs.call(i - 1, j, nk)
    b = dfs.call(i, j - 1, nk)
    res += [a, b].max
    f[i][j][kk] = res
    res
  end
  ans = dfs.call(m - 1, n - 1, k)
  ans < 0 ? -1 : ans
end
