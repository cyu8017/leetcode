# LeetCode 2942 - Find Words Containing Character
# https://leetcode.com/problems/find-words-containing-character/

# @param {String[]} words
# @param {Character} x
# @return {Integer[]}
def find_words_containing(words, x)
  ans = []
  words.each_with_index { |w, i| ans << i if w.include?(x) }
  ans
end
