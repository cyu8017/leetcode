# LeetCode 2185 - Counting Words With a Given Prefix
# https://leetcode.com/problems/counting-words-with-a-given-prefix/

# @param {String[]} words
# @param {String} pref
# @return {Integer}
def prefix_count(words, pref)
  words.count { |w| w.start_with?(pref) }
end
