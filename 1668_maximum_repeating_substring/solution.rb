# LeetCode 1668 - Maximum Repeating Substring
# https://leetcode.com/problems/maximum-repeating-substring/

# @param {String} sequence
# @param {String} word
# @return {Integer}
def max_repeating(sequence, word)
  k = 0
  k += 1 while sequence.include?(word * (k + 1))
  k
end
