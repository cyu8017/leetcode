# LeetCode 3084 - Count Substrings Starting and Ending with Given Character
# https://leetcode.com/problems/count-substrings-starting-and-ending-with-given-character/

# @param {String} s
# @param {String} c
# @return {Integer}
def count_substrings(s, c)
  cnt = s.chars.count { |ch| ch == c }
  cnt * (cnt + 1) / 2
end
