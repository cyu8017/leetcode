# LeetCode 3121 - Count the Number of Special Characters II
# https://leetcode.com/problems/count-the-number-of-special-characters-ii/

# @param {String} word
# @return {Integer}
def number_of_special_chars(word)
  first = Array.new(128, 0)
  last = Array.new(128, 0)
  word.each_char.with_index do |ch, i|
    c = ch.ord
    first[c] = i + 1 if first[c] == 0
    last[c] = i + 1
  end
  ans = 0
  26.times { |i| ans += 1 if last[97 + i] > 0 && last[97 + i] < first[65 + i] }
  ans
end
