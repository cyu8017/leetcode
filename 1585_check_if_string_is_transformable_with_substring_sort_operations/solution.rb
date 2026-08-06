# LeetCode 1585 - Check If String Is Transformable With Substring Sort Operations
# https://leetcode.com/problems/check-if-string-is-transformable-with-substring-sort-operations/

# @param {String} s
# @param {String} t
# @return {Boolean}
def is_transformable(s, t)
  positions = Array.new(10) { [] }
  s.each_char.with_index { |ch, i| positions[ch.to_i] << i }
  t.each_char do |ch|
    d = ch.to_i
    return false if positions[d].empty?
    index = positions[d][0]
    return false if (0...d).any? { |smaller| !positions[smaller].empty? && positions[smaller][0] < index }
    positions[d].shift
  end
  true
end
