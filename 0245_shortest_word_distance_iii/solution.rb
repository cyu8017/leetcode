# LeetCode 0245 - Shortest Word Distance III
# https://leetcode.com/problems/shortest-word-distance-iii/

# @param {String[]} words_dict
# @param {String} word1
# @param {String} word2
# @return {Integer}
def shortest_word_distance(words_dict, word1, word2)
  if word1 == word2
    previous = -1
    best = Float::INFINITY
    words_dict.each_with_index do |word, index|
      next unless word == word1

      best = [best, index - previous].min if previous >= 0
      previous = index
    end
    return best.to_i
  end

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
