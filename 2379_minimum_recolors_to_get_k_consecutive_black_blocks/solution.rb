# LeetCode 2379 - Minimum Recolors to Get K Consecutive Black Blocks
# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

# @param {String} blocks
# @param {Integer} k
# @return {Integer}
def minimum_recolors(blocks, k)
  white = 0
  (0...k).each { |i| white += 1 if blocks[i] == "W" }
  ans = white
  (k...blocks.length).each do |i|
    white += 1 if blocks[i] == "W"
    white -= 1 if blocks[i - k] == "W"
    ans = white if white < ans
  end
  ans
end
