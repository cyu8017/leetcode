# LeetCode 1540 - Can Convert String in K Moves
# https://leetcode.com/problems/can-convert-string-in-k-moves/

# @param {String} s
# @param {String} t
# @param {Integer} k
# @return {Boolean}
def can_convert_string(s, t, k)
  return false if s.length != t.length
  used = Array.new(26, 0)
  s.chars.zip(t.chars).each do |a, b|
    shift = (b.ord - a.ord) % 26
    next if shift == 0
    used[shift] += 1
    return false if shift + 26 * (used[shift] - 1) > k
  end
  true
end
