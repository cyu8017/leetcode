# LeetCode 1065 - Index Pairs of a String
# https://leetcode.com/problems/index-pairs-of-a-string/

# @param {String} text
# @param {String[]} words
# @return {Integer[][]}
def index_pairs(text, words)
  word_set = {}
  words.each { |w| word_set[w] = true }
  ans = []
  n = text.length
  (0...n).each do |i|
    (i...n).each do |j|
      ans << [i, j] if word_set[text[i..j]]
    end
  end
  ans
end
