# LeetCode 0472 - Concatenated Words
# https://leetcode.com/problems/concatenated-words/

class Solution
  def find_all_concatenated_words_in_a_dict(words)
    sorted = words.sort_by(&:length)
    word_set = sorted.to_set
    result = []

    can_form = lambda do |word, dictionary|
      return true if word.empty?

      length = word.length
      dp = Array.new(length + 1, false)
      dp[0] = true
      (1..length).each do |end_index|
        (0...end_index).each do |start|
          if dp[start] && dictionary.include?(word[start...end_index])
            dp[end_index] = true
            break
          end
        end
      end
      dp[length]
    end

    sorted.each do |word|
      word_set.delete(word)
      result << word if can_form.call(word, word_set)
      word_set.add(word)
    end
    result
  end

  alias_method :findAllConcatenatedWordsInADict, :find_all_concatenated_words_in_a_dict
end
