# LeetCode 0244 - Shortest Word Distance II
# https://leetcode.com/problems/shortest-word-distance-ii/

class WordDistance
  def initialize(words_dict)
    @positions = Hash.new { |hash, key| hash[key] = [] }
    words_dict.each_with_index do |word, index|
      @positions[word] << index
    end
  end

  def shortest(word1, word2)
    left = @positions[word1]
    right = @positions[word2]
    i = 0
    j = 0
    best = Float::INFINITY
    while i < left.length && j < right.length
      best = [best, (left[i] - right[j]).abs].min
      if left[i] <= right[j]
        i += 1
      else
        j += 1
      end
    end
    best.to_i
  end
end
