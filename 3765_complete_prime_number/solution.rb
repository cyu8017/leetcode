# LeetCode 3765 - Complete Prime Number
# https://leetcode.com/problems/complete-prime-number/

# @param {Integer} num
# @return {Boolean}
def complete_prime(num)
  is_prime = lambda do |x|
    return false if x < 2
    i = 2
    while i * i <= x
      return false if x % i == 0
      i += 1
    end
    true
  end
  s = num.to_s
  x = 0
  s.each_char do |c|
    x = x * 10 + (c.ord - 48)
    return false unless is_prime.call(x)
  end
  x = 0
  p = 1
  (s.length - 1).downto(0) do |i|
    x = p * (s[i].ord - 48) + x
    p *= 10
    return false unless is_prime.call(x)
  end
  true
end
