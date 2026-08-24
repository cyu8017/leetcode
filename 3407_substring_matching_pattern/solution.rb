# LeetCode 3407 - Substring Matching Pattern
# https://leetcode.com/problems/substring-matching-pattern/

# @param {String} s
# @param {String} p
# @return {Boolean}
def has_match(s, p)
  i = p.index("*")
  left = p[0...i]
  right = p[(i + 1)..]
  li = s.index(left)
  return false if li.nil?

  !s.index(right, li + left.length).nil?
end
