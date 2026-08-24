# LeetCode 2267 - Check if There Is a Valid Parentheses String Path
# https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/

# @param {String[][]} grid
# @return {Boolean}
def has_valid_path(grid)
  m = grid.length
  n = grid[0].length
  return false if (m + n - 1).odd? || grid[0][0] == ")" || grid[m - 1][n - 1] == "("

  vis = {}
  dfs = lambda do |r, c, bal|
    return false if r >= m || c >= n

    bal += grid[r][c] == "(" ? 1 : -1
    return false if bal < 0
    return bal == 0 if r == m - 1 && c == n - 1

    k = ((r * n + c) << 10) | bal
    return false if vis.key?(k)

    vis[k] = true
    dfs.call(r + 1, c, bal) || dfs.call(r, c + 1, bal)
  end
  dfs.call(0, 0, 0)
end
