# LeetCode 0771 - Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/

# @param {String} jewels
# @param {String} stones
# @return {Integer}
def num_jewels_in_stones(jewels, stones)
  jewel_set = {}
  jewels.each_char { |ch| jewel_set[ch] = true }
  stones.chars.count { |stone| jewel_set[stone] }
end
