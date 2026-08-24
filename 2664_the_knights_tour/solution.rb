# LeetCode 2664 - The Knight's Tour
# https://leetcode.com/problems/the-knights-tour/

# @param {Integer} m
# @param {Integer} n
# @param {Integer} r
# @param {Integer} c
# @return {Integer[][]}
def tour_of_knight(m, n, r, c)
  dirs = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]
  ans = Array.new(m) { Array.new(n, -1) }
  dfs = nil
  dfs = lambda do |x, y, step|
    ans[x][y] = step
    return true if step == m * n - 1

    dirs.each do |dx, dy|
      nx = x + dx
      ny = y + dy
      if nx >= 0 && nx < m && ny >= 0 && ny < n && ans[nx][ny] == -1
        return true if dfs.call(nx, ny, step + 1)
      end
    end
    ans[x][y] = -1
    false
  end
  dfs.call(r, c, 0)
  ans
end

def solve(*args)
  tour_of_knight(*args)
end
