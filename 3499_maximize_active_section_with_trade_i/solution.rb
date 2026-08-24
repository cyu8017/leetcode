# LeetCode 3499 - Maximize Active Section with Trade I
# https://leetcode.com/problems/maximize-active-section-with-trade-i/

# @param {String} s
# @return {Integer}
def max_active_sections_after_trade(s)
  ones = 0
  s.each_char { |c| ones += 1 if c == "1" }
  zeros = []
  n = s.length
  i = 0
  while i < n
    if s[i] != "0"
      i += 1
      next
    end
    j = i
    j += 1 while j < n && s[j] == "0"
    zeros << [i, j - 1]
    i = j
  end
  best = 0
  (0...(zeros.length - 1)).each do |i|
    gain = (zeros[i][1] - zeros[i][0] + 1) + (zeros[i + 1][1] - zeros[i + 1][0] + 1)
    best = gain if gain > best
  end
  ones + best
end
