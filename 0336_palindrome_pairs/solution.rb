# LeetCode 0336 - Palindrome Pairs
# https://leetcode.com/problems/palindrome-pairs/

class Solution
  def palindrome_pairs(words)
    word_map = {}
    words.each_with_index { |word, index| word_map[word] = index }
    result = {}

    words.each_with_index do |word, index|
      (0..word.length).each do |split|
        left = word[0...split]
        right = word[split..]
        if left == left.reverse
          reversed_right = right.reverse
          if word_map.key?(reversed_right) && word_map[reversed_right] != index
            result[[word_map[reversed_right], index]] = true
          end
        end
        if right == right.reverse
          reversed_left = left.reverse
          if word_map.key?(reversed_left) && word_map[reversed_left] != index
            result[[index, word_map[reversed_left]]] = true
          end
        end
      end
    end

    result.keys.sort
  end

  alias_method :palindromePairs, :palindrome_pairs
end
