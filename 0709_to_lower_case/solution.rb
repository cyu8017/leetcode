# LeetCode 0709 - To Lower Case
# https://leetcode.com/problems/to-lower-case/

# @param {String} s
# @return {String}
def to_lower_case(s)
  s.chars.map { |ch| ch >= "A" && ch <= "Z" ? (ch.ord + 32).chr : ch }.join
end
