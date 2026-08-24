# LeetCode 3750 - Minimum Number of Flips to Reverse Binary String
# https://leetcode.com/problems/minimum-number-of-flips-to-reverse-binary-string/

# @param {Integer} n
# @return {Integer}
def minimum_flips(n)
  x = n
  if x == 0
    s = "0"
  else
    bits = []
    while x > 0
      bits << (48 + (x & 1)).chr
      x >>= 1
    end
    s = bits.reverse.join
  end
  m = s.length
  cnt = 0
  (0...(m / 2)).each { |i| cnt += 1 if s[i] != s[m - i - 1] }
  cnt * 2
end
