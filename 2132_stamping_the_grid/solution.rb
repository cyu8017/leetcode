# LeetCode 2132 - Stamping the Grid
# https://leetcode.com/problems/stamping-the-grid/

# @param {Integer[][]} grid
# @param {Integer} stamp_height
# @param {Integer} stamp_width
# @return {Boolean}
def possible_to_stamp(grid, stamp_height, stamp_width)
  m = grid.length
  n = grid[0].length
  pref = Array.new(m + 1) { Array.new(n + 1, 0) }
  m.times do |i|
    n.times do |j|
      pref[i + 1][j + 1] = pref[i + 1][j] + pref[i][j + 1] - pref[i][j] + grid[i][j]
    end
  end
  diff = Array.new(m + 1) { Array.new(n + 1, 0) }
  i = 0
  while i + stamp_height - 1 < m
    j = 0
    while j + stamp_width - 1 < n
      sum = pref[i + stamp_height][j + stamp_width] - pref[i][j + stamp_width] - pref[i + stamp_height][j] + pref[i][j]
      if sum == 0
        diff[i][j] += 1
        diff[i][j + stamp_width] -= 1
        diff[i + stamp_height][j] -= 1
        diff[i + stamp_height][j + stamp_width] += 1
      end
      j += 1
    end
    i += 1
  end
  cur = Array.new(m) { Array.new(n, 0) }
  m.times do |i|
    n.times do |j|
      v = diff[i][j]
      v += cur[i - 1][j] if i > 0
      v += cur[i][j - 1] if j > 0
      v -= cur[i - 1][j - 1] if i > 0 && j > 0
      cur[i][j] = v
      return false if grid[i][j] == 0 && v == 0
    end
  end
  true
end
