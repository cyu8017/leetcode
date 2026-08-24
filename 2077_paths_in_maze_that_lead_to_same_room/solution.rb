# LeetCode 2077 - Paths in Maze That Lead to Same Room
# https://leetcode.com/problems/paths-in-maze-that-lead-to-same-room/

# @param {Integer} n
# @param {Integer[][]} corridors
# @return {Integer}
def number_of_paths(n, corridors)
  g = Array.new(n + 1) { {} }
  corridors.each do |a, b|
    g[a][b] = true
    g[b][a] = true
  end
  ans = 0
  corridors.each do |a, b|
    g[a].each_key { |c| ans += 1 if g[b][c] }
  end
  ans / 3
end

alias solve number_of_paths
