# LeetCode 1078 - Occurrences After Bigram
# https://leetcode.com/problems/occurrences-after-bigram/

# @param {String} text
# @param {String} first
# @param {String} second
# @return {String[]}
def find_ocurrences(text, first, second)
  words = text.split
  (0...(words.length - 2)).filter_map do |i|
    words[i + 2] if words[i] == first && words[i + 1] == second
  end
end
