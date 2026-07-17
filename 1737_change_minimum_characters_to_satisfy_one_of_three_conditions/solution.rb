# LeetCode 1737 - Change Minimum Characters to Satisfy One of Three Conditions
# https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/

# @param {String} a
# @param {String} b
# @return {Integer}
def min_characters(a, b)
  ca = Array.new(26, 0)
  cb = Array.new(26, 0)
  a.each_char { |ch| ca[ch.ord - 97] += 1 }
  b.each_char { |ch| cb[ch.ord - 97] += 1 }
  n = a.length
  m = b.length
  ans = n + m - [ca.max, cb.max].max
  pre_a = 0
  pre_b = 0
  (0...25).each do |code|
    pre_a += ca[code]
    pre_b += cb[code]
    ans = [ans, n - pre_a + pre_b, m - pre_b + pre_a].min
  end
  ans
end
