# LeetCode 1758 - Minimum Changes To Make Alternating Binary String
# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

# @param {String} s
# @return {Integer}
def min_operations(s)
  alt1 = 0
  s.each_char.with_index do |ch, i|
    expected = i.even? ? '0' : '1'
    alt1 += 1 if ch != expected
  end
  [alt1, s.length - alt1].min
end
