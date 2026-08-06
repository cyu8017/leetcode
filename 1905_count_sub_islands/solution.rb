# LeetCode 1905 - Count Sub Islands
# https://leetcode.com/problems/count-sub-islands/

# @param {Integer[][]} grid1
# @param {Integer[][]} grid2
# @return {Integer}
def count_sub_islands(grid1, grid2)
  rows = grid2.length
  cols = grid2[0].length

  dfs = lambda do |r, c|
    return true if r < 0 || c < 0 || r >= rows || c >= cols || grid2[r][c].zero?
    grid2[r][c] = 0
    ok = grid1[r][c] == 1
    [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]].each do |nr, nc|
      ok = false unless dfs.call(nr, nc)
    end
    ok
  end

  ans = 0
  rows.times do |r|
    cols.times do |c|
      ans += 1 if grid2[r][c] == 1 && dfs.call(r, c)
    end
  end
  ans
end
