# LeetCode 1992 - Find All Groups of Farmland
# https://leetcode.com/problems/find-all-groups-of-farmland/

# @param {Integer[][]} land
# @return {Integer[][]}
def find_farmland(land)
  m = land.length
  n = land[0].length
  ans = []
  m.times do |i|
    n.times do |j|
      next unless land[i][j] == 1 && (i.zero? || land[i - 1][j].zero?) && (j.zero? || land[i][j - 1].zero?)
      r = i
      c = j
      r += 1 while r + 1 < m && land[r + 1][j] == 1
      c += 1 while c + 1 < n && land[i][c + 1] == 1
      ans << [i, j, r, c]
    end
  end
  ans
end
