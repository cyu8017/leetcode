# LeetCode 2000 - Reverse Prefix of Word
# https://leetcode.com/problems/reverse-prefix-of-word/

# @param {String} word
# @param {Character} ch
# @return {String}
def reverse_prefix(word, ch)
  i = word.index(ch)
  return word if i.nil?

  word[0..i].reverse + word[i + 1..]
end
