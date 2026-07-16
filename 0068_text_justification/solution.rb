# LeetCode 0068 - Text Justification
# https://leetcode.com/problems/text-justification/

# @param {String[]} words
# @param {Integer} max_width
# @return {String[]}
def full_justify(words, max_width)
  result = []
  i = 0

  while i < words.length
    line_words = []
    line_len = 0

    while i < words.length
      word = words[i]
      extra = line_words.empty? ? 0 : 1
      break if line_len + word.length + extra > max_width

      line_words << word
      line_len += word.length + extra
      i += 1
    end

    if i == words.length || line_words.length == 1
      line = line_words.join(' ')
      line += ' ' * (max_width - line.length)
      result << line
    else
      total_chars = line_words.sum(&:length)
      total_spaces = max_width - total_chars
      gaps = line_words.length - 1
      space, remainder = total_spaces.divmod(gaps)
      line = ''
      line_words[0...-1].each_with_index do |word, j|
        line += word + (' ' * (space + (j < remainder ? 1 : 0)))
      end
      line += line_words[-1]
      result << line
    end
  end

  result
end
