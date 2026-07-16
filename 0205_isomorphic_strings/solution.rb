# LeetCode 0205 - Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/

# @param {String} s
# @param {String} t
# @return {Boolean}
def is_isomorphic(s, t)
  return false unless s.length == t.length

  forward = {}
  backward = {}
  s.chars.zip(t.chars).each do |a, b|
    return false if forward.key?(a) && forward[a] != b
    return false if backward.key?(b) && backward[b] != a

    forward[a] = b
    backward[b] = a
  end
  true
end