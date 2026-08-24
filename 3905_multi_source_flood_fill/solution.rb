# LeetCode 3905 - Multi Source Flood Fill
# https://leetcode.com/problems/multi-source-flood-fill/

# @param {Integer} n
# @param {Integer} m
# @param {Integer[][]} sources
# @return {Integer[][]}
def color_grid(n, m, sources)
  ans = Array.new(n) { Array.new(m, 0) }
  q = sources.map(&:dup)
  dirs = [-1, 0, 1, 0, -1]
  q.each { |s| ans[s[0]][s[1]] = s[2] }
  until q.empty?
    vis = {}
    q.each do |curr|
      r, c, color = curr[0], curr[1], curr[2]
      4.times do |i|
        x = r + dirs[i]
        y = c + dirs[i + 1]
        if x >= 0 && x < n && y >= 0 && y < m && ans[x][y] == 0
          key = (x << 32) | (y & 0xFFFFFFFF)
          vis[key] = color if !vis.key?(key) || color > vis[key]
        end
      end
    end
    q = []
    vis.each do |key, color|
      x = key >> 32
      y = key & 0xFFFFFFFF
      ans[x][y] = color
      q << [x, y, color]
    end
  end
  ans
end
