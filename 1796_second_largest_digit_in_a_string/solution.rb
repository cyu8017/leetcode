# LeetCode 1796 - Second Largest Digit in a String
# https://leetcode.com/problems/second-largest-digit-in-a-string/

# @param {String} s
# @return {Integer}
def second_highest(s)
  digits = s.chars.select { |ch| ch =~ /\d/ }.map(&:to_i).uniq.sort
  digits.length > 1 ? digits[-2] : -1
end
