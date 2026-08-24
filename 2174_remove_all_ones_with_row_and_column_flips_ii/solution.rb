# LeetCode 2174 - Remove All Ones With Row and Column Flips II
# https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips-ii/

# @param {Integer[][]} grid
# @return {Integer}
def remove_ones(grid)
  m = grid.length
  n = grid[0].length
  ones = []
  m.times do |i|
    n.times { |j| ones << [i, j] if grid[i][j] == 1 }
  end
  return 0 if ones.empty?

  ans = m + n
  dfs = nil
  dfs = lambda do |idx, flips|
    return if flips >= ans

    idx += 1 while idx < ones.length && grid[ones[idx][0]][ones[idx][1]] == 0
    if idx == ones.length
      ans = flips
      return
    end
    r, c = ones[idx]
    changed = []
    n.times do |j|
      if grid[r][j] == 1
        grid[r][j] = 0
        changed << [r, j]
      end
    end
    dfs.call(idx + 1, flips + 1)
    changed.each { |x, y| grid[x][y] = 1 }
    changed = []
    m.times do |i|
      if grid[i][c] == 1
        grid[i][c] = 0
        changed << [i, c]
      end
    end
    dfs.call(idx + 1, flips + 1)
    changed.each { |x, y| grid[x][y] = 1 }
  end
  dfs.call(0, 0)
  ans
end
