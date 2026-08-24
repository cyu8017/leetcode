# LeetCode 2114 - Maximum Number of Words Found in Sentences
# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

# @param {String[]} sentences
# @return {Integer}
def most_words_found(sentences)
  sentences.map { |s| s.count(" ") + 1 }.max
end
