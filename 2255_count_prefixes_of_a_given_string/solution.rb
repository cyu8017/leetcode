# LeetCode 2255 - Count Prefixes of a Given String
# https://leetcode.com/problems/count-prefixes-of-a-given-string/

# @param {String[]} words
# @param {String} s
# @return {Integer}
def count_prefixes(words, s)
  words.count { |w| w.length <= s.length && s.start_with?(w) }
end
