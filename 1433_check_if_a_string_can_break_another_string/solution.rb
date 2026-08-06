# LeetCode 1433 - Check If A String Can Break Another String
# https://leetcode.com/problems/check-if-a-string-can-break-another-string/

def check_if_can_break(s1, s2)
  a = s1.chars.sort
  b = s2.chars.sort
  a.zip(b).all? { |x, y| x >= y } || a.zip(b).all? { |x, y| x <= y }
end
