# LeetCode 1020 - Number of Enclaves
# https://leetcode.com/problems/number-of-enclaves/

# @param {Integer[][]} grid
# @return {Integer}
def num_enclaves(grid)
  m = grid.length
  n = grid[0].length

  dfs = lambda do |r, c|
    return if r.negative? || r >= m || c.negative? || c >= n || grid[r][c] != 1

    grid[r][c] = 0
    dfs.call(r + 1, c)
    dfs.call(r - 1, c)
    dfs.call(r, c + 1)
    dfs.call(r, c - 1)
  end

  m.times do |i|
    dfs.call(i, 0)
    dfs.call(i, n - 1)
  end
  n.times do |j|
    dfs.call(0, j)
    dfs.call(m - 1, j)
  end
  grid.sum(&:sum)
end
