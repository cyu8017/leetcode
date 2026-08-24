# LeetCode 2429 - Minimize XOR
# https://leetcode.com/problems/minimize-xor/

# @param {Integer} num1
# @param {Integer} num2
# @return {Integer}
def minimize_xor(num1, num2)
  bits = 0
  x = num2
  while x != 0
    x &= x - 1
    bits += 1
  end
  ans = 0
  31.downto(0) do |i|
    break if bits <= 0
    next if ((num1 >> i) & 1) == 0

    ans |= 1 << i
    bits -= 1
  end
  (0...32).each do |i|
    break if bits <= 0
    next if ((ans >> i) & 1) != 0

    ans |= 1 << i
    bits -= 1
  end
  ans
end
