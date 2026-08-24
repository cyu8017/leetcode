# LeetCode 2083 - Substrings That Begin and End With the Same Letter
# https://leetcode.com/problems/substrings-that-begin-and-end-with-the-same-letter/

# @param {String} s
# @return {Integer}
def number_of_substrings(s)
  freq = Array.new(26, 0)
  ans = 0
  s.each_char do |c|
    i = c.ord - 97
    freq[i] += 1
    ans += freq[i]
  end
  ans
end

alias solve number_of_substrings
