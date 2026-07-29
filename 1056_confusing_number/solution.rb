# LeetCode 1056 - Confusing Number
# https://leetcode.com/problems/confusing-number/

# @param {Integer} n
# @return {Boolean}
def confusing_number(n)
  rotate = { "0" => "0", "1" => "1", "6" => "9", "8" => "8", "9" => "6" }
  s = n.to_s
  rotated = +""
  s.reverse.each_char do |ch|
    return false unless rotate.key?(ch)

    rotated << rotate[ch]
  end
  rotated != s
end
