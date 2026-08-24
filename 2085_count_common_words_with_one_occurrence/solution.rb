# LeetCode 2085 - Count Common Words With One Occurrence
# https://leetcode.com/problems/count-common-words-with-one-occurrence/

# @param {String[]} words1
# @param {String[]} words2
# @return {Integer}
def count_words(words1, words2)
  f1 = Hash.new(0)
  f2 = Hash.new(0)
  words1.each { |w| f1[w] += 1 }
  words2.each { |w| f2[w] += 1 }
  f1.count { |k, v| v == 1 && f2[k] == 1 }
end
