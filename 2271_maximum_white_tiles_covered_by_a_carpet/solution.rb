# LeetCode 2271 - Maximum White Tiles Covered by a Carpet
# https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/

# @param {Integer[][]} tiles
# @param {Integer} carpet_len
# @return {Integer}
def maximum_white_tiles(tiles, carpet_len)
  tiles = tiles.sort_by { |t| t[0] }
  n = tiles.length
  pref = Array.new(n + 1, 0)
  n.times { |i| pref[i + 1] = pref[i] + (tiles[i][1] - tiles[i][0] + 1) }
  ans = 0
  j = 0
  n.times do |i|
    last = tiles[i][0] + carpet_len - 1
    j += 1 while j < n && tiles[j][0] <= last
    cover = pref[j] - pref[i]
    cover -= tiles[j - 1][1] - last if j > 0 && tiles[j - 1][1] > last
    ans = [ans, cover].max
  end
  ans
end
