# LeetCode 0858 - Mirror Reflection
# https://leetcode.com/problems/mirror-reflection/

# @param {Integer} p
# @param {Integer} q
# @return {Integer}
def mirror_reflection(p, q)
  g = p.gcd(q)
  p /= g
  q /= g
  return 2 if p.even?
  return 0 if q.even?

  1
end
