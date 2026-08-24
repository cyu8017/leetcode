# LeetCode 2116 - Check if a Parentheses String Can Be Valid
# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/

# @param {String} s
# @param {String} locked
# @return {Boolean}
def can_be_valid(s, locked)
  n = s.length
  return false if n.odd?

  bal = 0
  n.times do |i|
    bal += locked[i] == "0" || s[i] == "(" ? 1 : -1
    return false if bal < 0
  end
  bal = 0
  (n - 1).downto(0) do |i|
    bal += locked[i] == "0" || s[i] == ")" ? 1 : -1
    return false if bal < 0
  end
  true
end
