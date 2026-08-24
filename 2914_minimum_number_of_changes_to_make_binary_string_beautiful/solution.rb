# LeetCode 2914 - Minimum Number of Changes to Make Binary String Beautiful
# https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/

# @param {String} s
# @return {Integer}
def min_changes(s)
  ans = 0
  0.step(s.length - 1, 2) { |i| ans += 1 if s[i] != s[i + 1] }
  ans
end
