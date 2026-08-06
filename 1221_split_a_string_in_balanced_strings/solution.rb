# LeetCode 1221 - Split a String in Balanced Strings
# https://leetcode.com/problems/split-a-string-in-balanced-strings/

# @param {String} s
# @return {Integer}
def balanced_string_split(s)
  balance = answer = 0
  s.each_char do |ch|
    balance += ch == "L" ? 1 : -1
    answer += 1 if balance == 0
  end
  answer
end
