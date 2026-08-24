# LeetCode 3754 - Concatenate Non Zero Digits and Multiply by Sum I
# https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/

# @param {Integer} n
# @return {Integer}
def sum_and_multiply(n)
  p = 1
  x = 0
  s = 0
  while n > 0
    v = n % 10
    if v != 0
      s += v
      x += p * v
      p *= 10
    end
    n /= 10
  end
  x * s
end
