# LeetCode 0161 - One Edit Distance
# https://leetcode.com/problems/one-edit-distance/

class Solution
  def is_one_edit_distance(s, t)
    return false if (s.length - t.length).abs > 1 || s == t

    s, t = t, s if s.length > t.length
    index = 0
    index += 1 while index < s.length && s[index] == t[index]
    s.length == t.length ? s[(index + 1)..] == t[(index + 1)..] : s[index..] == t[(index + 1)..]
  end
end