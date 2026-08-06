# LeetCode 1239 - Maximum Length of a Concatenated String with Unique Characters
# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

# @param {String[]} arr
# @return {Integer}
def max_length(arr)
  masks = [[0, 0]]
  arr.each do |word|
    mask = 0
    word.each_char { |ch| mask |= 1 << (ch.ord - 97) }
    next if mask.to_s(2).count("1") != word.length
    masks += masks.select { |used, _| (used & mask).zero? }.map { |used, length| [used | mask, length + word.length] }
  end
  masks.map(&:last).max
end
