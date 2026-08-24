# LeetCode 2596 - Check Knight Tour Configuration
# https://leetcode.com/problems/check-knight-tour-configuration/

# @param {Integer[][]} grid
# @return {Boolean}
def check_valid_grid(grid)
  n = grid.length
  return false if grid[0][0] != 0

  pos = Array.new(n * n)
  n.times do |i|
    n.times do |j|
      pos[grid[i][j]] = [i, j]
    end
  end
  dirs = [
    [1, 2], [1, -2], [-1, 2], [-1, -2],
    [2, 1], [2, -1], [-2, 1], [-2, -1]
  ]
  (n * n - 1).times do |v|
    r, c = pos[v]
    ok = false
    dirs.each do |dr, dc|
      if r + dr == pos[v + 1][0] && c + dc == pos[v + 1][1]
        ok = true
        break
      end
    end
    return false unless ok
  end
  true
end
