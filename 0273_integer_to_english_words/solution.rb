# LeetCode 0273 - Integer to English Words
# https://leetcode.com/problems/integer-to-english-words/

ONES = [
  "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
  "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
  "Seventeen", "Eighteen", "Nineteen"
].freeze
TENS = [
  "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
].freeze
THOUSANDS = ["", "Thousand", "Million", "Billion"].freeze

def convert_chunk(value)
  return "" if value == 0
  return ONES[value] if value < 20
  if value < 100
    tens = TENS[value / 10]
    ones = ONES[value % 10]
    return ones.empty? ? tens : "#{tens} #{ones}"
  end
  hundreds = ONES[value / 100]
  remainder = convert_chunk(value % 100)
  remainder.empty? ? "#{hundreds} Hundred" : "#{hundreds} Hundred #{remainder}"
end

# @param {Integer} num
# @return {String}
def number_to_words(num)
  return "Zero" if num == 0

  parts = []
  chunk_index = 0
  while num > 0
    chunk = num % 1000
    if chunk != 0
      chunk_words = convert_chunk(chunk)
      chunk_words += " #{THOUSANDS[chunk_index]}" unless THOUSANDS[chunk_index].empty?
      parts << chunk_words
    end
    num /= 1000
    chunk_index += 1
  end
  parts.reverse.join(" ")
end
