# LeetCode 0418 - Sentence Screen Fitting
# https://leetcode.com/problems/sentence-screen-fitting/

class Solution
  def words_typing(sentence, rows, cols)
    count = 0
    index = 0
    total = sentence.length

    rows.times do
      col = 0
      loop do
        word = sentence[index]
        needed = word.length + (col.positive? ? 1 : 0)
        break if col + needed > cols

        col += 1 if col.positive?
        col += word.length
        index = (index + 1) % total
        count += 1 if index.zero?
      end
    end

    count
  end

  alias_method :wordsTyping, :words_typing
end
