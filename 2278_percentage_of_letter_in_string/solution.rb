# LeetCode 2278 - Percentage of Letter in String
# https://leetcode.com/problems/percentage-of-letter-in-string/

# @param {String} s
# @param {String} letter
# @return {Integer}
def percentage_letter(s, letter)
  cnt = 0
  s.each_char { |c| cnt += 1 if c == letter }
  cnt * 100 / s.length
end
