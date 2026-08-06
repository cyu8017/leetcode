# LeetCode 1408 - String Matching In An Array
# https://leetcode.com/problems/string-matching-in-an-array/

def string_matching(words)
  words.select.with_index { |word, i| words.each_with_index.any? { |other, j| i != j && other.include?(word) } }
end
