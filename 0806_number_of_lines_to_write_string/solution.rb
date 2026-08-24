# LeetCode 0806 - Number of Lines To Write String
# https://leetcode.com/problems/number-of-lines-to-write-string/

# @param {Integer[]} widths
# @param {String} s
# @return {Integer[]}
def number_of_lines(widths, s)
  lines = 1
  width = 0
  s.each_char do |ch|
    w = widths[ch.ord - 97]
    if width + w > 100
      lines += 1
      width = w
    else
      width += w
    end
  end
  [lines, width]
end
