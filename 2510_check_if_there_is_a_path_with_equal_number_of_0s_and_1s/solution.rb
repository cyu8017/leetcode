# LeetCode 2510 - Check if There is a Path With Equal Number of 0's And 1's
# https://leetcode.com/problems/check-if-there-is-a-path-with-equal-number-of-0s-and-1s/

# @param {Integer[][]} grid
# @return {Boolean}
def is_there_a_path(grid)
  m = grid.length
  n = grid[0].length
  return false if (m + n - 1).odd?

  target = (m + n - 1) / 2
  memo = {}

  dfs = lambda do |r, c, bal|
    return false if r >= m || c >= n

    bal += grid[r][c]
    return false if bal > target || bal + (m - 1 - r) + (n - 1 - c) < target
    return bal == target if r == m - 1 && c == n - 1

    key = [r, c, bal]
    return memo[key] if memo.key?(key)

    ok = dfs.call(r + 1, c, bal) || dfs.call(r, c + 1, bal)
    memo[key] = ok
    ok
  end

  dfs.call(0, 0, 0)
end
