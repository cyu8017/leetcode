# LeetCode 1768 - Merge Strings Alternately
# https://leetcode.com/problems/merge-strings-alternately/

# @param {String} word1
# @param {String} word2
# @return {String}
def merge_alternately(word1, word2)
  out = []
  i = 0
  j = 0
  while i < word1.length || j < word2.length
    if i < word1.length
      out << word1[i]
      i += 1
    end
    if j < word2.length
      out << word2[j]
      j += 1
    end
  end
  out.join
end
