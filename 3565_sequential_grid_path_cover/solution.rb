# LeetCode 3565 - Sequential Grid Path Cover
# https://leetcode.com/problems/sequential-grid-path-cover/

# @param {Integer[][]} grid
# @param {Integer} k
# @return {Integer[][]}
def find_path(grid, k)
  m = grid.length
  n = grid[0].length
  dirs = [-1, 0, 1, 0, -1]
  st = [0]
  path = []
  f = lambda { |i, j| i * n + j }
  dfs = nil
  dfs = lambda do |i, j, v|
    path << [i, j]
    return true if path.length == m * n
    idx = f.call(i, j)
    st[0] |= 1 << idx
    v += 1 if grid[i][j] == v
    (0...4).each do |t|
      x = i + dirs[t]
      y = j + dirs[t + 1]
      if x >= 0 && x < m && y >= 0 && y < n
        idx2 = f.call(x, y)
        if ((st[0] >> idx2) & 1) == 0 && (grid[x][y] == 0 || grid[x][y] == v)
          return true if dfs.call(x, y, v)
        end
      end
    end
    path.pop
    st[0] ^= 1 << idx
    false
  end
  (0...m).each do |i|
    (0...n).each do |j|
      if grid[i][j] == 0 || grid[i][j] == 1
        return path if dfs.call(i, j, 1)
        path.clear
        st[0] = 0
      end
    end
  end
  []
end
