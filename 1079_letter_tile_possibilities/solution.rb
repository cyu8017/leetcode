# LeetCode 1079 - Letter Tile Possibilities
# https://leetcode.com/problems/letter-tile-possibilities/

# @param {String} tiles
# @return {Integer}
def num_tile_possibilities(tiles)
  count = Hash.new(0)
  tiles.each_char { |ch| count[ch] += 1 }

  dfs = lambda do
    total = 0
    count.each_key do |ch|
      next if count[ch].zero?

      count[ch] -= 1
      total += 1 + dfs.call
      count[ch] += 1
    end
    total
  end

  dfs.call
end
