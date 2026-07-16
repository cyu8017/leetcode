# LeetCode 0030 - Substring with Concatenation of All Words
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

# @param {String} s
# @param {String[]} words
# @return {Integer[]}
def find_substring(s, words)
  return [] if words.empty? || s.empty?

  word_len = words[0].length
  word_count = words.length
  need = words.tally
  result = []

  (0...word_len).each do |start|
    left = start
    counts = Hash.new(0)
    used = 0

    right = start
    while right <= s.length - word_len
      word = s[right, word_len]
      unless need.key?(word)
        counts = Hash.new(0)
        used = 0
        left = right + word_len
        right = left
        next
      end

      counts[word] += 1
      used += 1
      while counts[word] > need[word]
        left_word = s[left, word_len]
        counts[left_word] -= 1
        used -= 1
        left += word_len
      end

      result << left if used == word_count
      right += word_len
    end
  end

  result.sort
end
