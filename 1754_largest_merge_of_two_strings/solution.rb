# LeetCode 1754 - Largest Merge Of Two Strings
# https://leetcode.com/problems/largest-merge-of-two-strings/

# @param {String} word1
# @param {String} word2
# @return {String}
def largest_merge(word1, word2)
  i = 0
  j = 0
  out = []
  while i < word1.length && j < word2.length
    if word1[i..] > word2[j..]
      out << word1[i]
      i += 1
    else
      out << word2[j]
      j += 1
    end
  end
  out.join + word1[i..] + word2[j..]
end
