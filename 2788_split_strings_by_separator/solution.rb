# LeetCode 2788 - Split Strings by Separator
# https://leetcode.com/problems/split-strings-by-separator/

# @param {String[]} words
# @param {String} separator
# @return {String[]}
def split_words_by_separator(words, separator)
  ans = []
  words.each do |w|
    start = 0
    (0..w.length).each do |i|
      if i == w.length || w[i] == separator
        ans << w[start...i] if i > start
        start = i + 1
      end
    end
  end
  ans
end
