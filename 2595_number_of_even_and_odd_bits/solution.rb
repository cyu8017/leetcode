# LeetCode 2595 - Number of Even and Odd Bits
# https://leetcode.com/problems/number-of-even-and-odd-bits/

# @param {Integer} n
# @return {Integer[]}
def even_odd_bit(n)
  even = 0
  odd = 0
  i = 0
  while n > 0
    if (n & 1) != 0
      if i.even?
        even += 1
      else
        odd += 1
      end
    end
    i += 1
    n >>= 1
  end
  [even, odd]
end
