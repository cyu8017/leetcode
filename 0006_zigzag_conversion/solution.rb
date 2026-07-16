# LeetCode 0006 - Zigzag Conversion
# https://leetcode.com/problems/zigzag-conversion/

# @param {String} s
# @param {Integer} num_rows
# @return {String}
def convert(s, num_rows)
  return s if num_rows == 1 || num_rows >= s.length

  rows = Array.new(num_rows, +"")
  index = 0
  step = 1

  s.each_char do |ch|
    rows[index] << ch
    if index.zero?
      step = 1
    elsif index == num_rows - 1
      step = -1
    end
    index += step
  end

  rows.join
end
