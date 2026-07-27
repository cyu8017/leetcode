# LeetCode 1657 - Determine if Two Strings Are Close
# https://leetcode.com/problems/determine-if-two-strings-are-close/

# @param {String} word1
# @param {String} word2
# @return {Boolean}
def close_strings(word1, word2)
  a = Hash.new(0)
  b = Hash.new(0)
  word1.each_char { |c| a[c] += 1 }
  word2.each_char { |c| b[c] += 1 }
  a.keys.sort == b.keys.sort && a.values.sort == b.values.sort
end
