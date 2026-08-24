# LeetCode 3746 - Minimum String Length After Balanced Removals
# https://leetcode.com/problems/minimum-string-length-after-balanced-removals/

# @param {String} s
# @return {Integer}
def min_length_after_removals(s)
  a = s.each_char.count { |ch| ch == "a" }
  b = s.length - a
  (a - b).abs
end
