# LeetCode 3797 - Count Routes to Climb a Rectangular Grid
# https://leetcode.com/problems/count-routes-to-climb-a-rectangular-grid/

# @param {String[][]} grid
# @param {Integer} d
# @return {Integer}
def count_routes(grid, d)
  mod = 1_000_000_007
  n = grid.length
  m = grid[0].length
  up_radius = 0
  up_radius += 1 while (up_radius + 1) * (up_radius + 1) + 1 <= d * d
  arrived = Array.new(m, 0)
  (0...m).each { |c| arrived[c] = 1 if grid[n - 1][c] == "." }
  (n - 1).downto(0) do |r|
    pref = Array.new(m + 1, 0)
    (0...m).each { |i| pref[i + 1] = (pref[i] + arrived[i]) % mod }
    horizontal = Array.new(m, 0)
    (0...m).each do |c|
      next if grid[r][c] == "#"
      l = [0, c - d].max
      rr = [m - 1, c + d].min
      horizontal[c] = (pref[rr + 1] - pref[l] - arrived[c]) % mod
      horizontal[c] += mod if horizontal[c] < 0
    end
    if r == 0
      ans = 0
      (0...m).each { |c| ans = (ans + arrived[c] + horizontal[c]) % mod }
      return ans
    end
    pref2 = Array.new(m + 1, 0)
    (0...m).each { |c| pref2[c + 1] = (pref2[c] + arrived[c] + horizontal[c]) % mod }
    nxt = Array.new(m, 0)
    (0...m).each do |c|
      next if grid[r - 1][c] == "#"
      l = [0, c - up_radius].max
      rr = [m - 1, c + up_radius].min
      nxt[c] = pref2[rr + 1] - pref2[l]
      nxt[c] += mod if nxt[c] < 0
    end
    arrived = nxt
  end
  0
end
