# LeetCode 0243 - Shortest Word Distance
# https://leetcode.com/problems/shortest-word-distance/

# @param {String[]} words_dict
# @param {String} word1
# @param {String} word2
# @return {Integer}
def shortest_word_distance(words_dict, word1, word2)
  index1 = -1
  index2 = -1
  best = Float::INFINITY
  words_dict.each_with_index do |word, index|
    if word == word1
      index1 = index
      best = [best, index - index2].min if index2 >= 0
    end
    if word == word2
      index2 = index
      best = [best, index - index1].min if index1 >= 0
    end
  end
  best.to_i
end
