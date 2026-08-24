# LeetCode 2556 - Disconnect Path in a Binary Matrix by at Most One Flip
# https://leetcode.com/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/

# @param {Integer[][]} grid
# @return {Boolean}
def is_possible_to_cut_path(grid)
  m = grid.length
  n = grid[0].length

  dfs = lambda do |r, c|
    return true if r == m - 1 && c == n - 1
    return false if r >= m || c >= n || grid[r][c] == 0

    grid[r][c] = 0 unless r == 0 && c == 0
    dfs.call(r + 1, c) || dfs.call(r, c + 1)
  end

  return true unless dfs.call(0, 0)

  grid[0][0] = 1
  !dfs.call(0, 0)
end
