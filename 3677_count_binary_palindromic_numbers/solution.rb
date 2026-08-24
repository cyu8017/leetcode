# LeetCode 3677 - Count Binary Palindromic Numbers
# https://leetcode.com/problems/count-binary-palindromic-numbers/

# @param {Integer} n
# @return {Integer}
def count_binary_palindromes(n)
  return 1 if n == 0

  ans = 1
  s = ""
  x = n
  while x > 0
    s += (x & 1).to_s
    x /= 2
  end
  s = s.reverse
  l = s.length
  (1...l).each do |length|
    half = (length + 1) / 2
    ans += 1 << (half - 1)
  end
  half = (l + 1) / 2
  prefix = s[0, half]
  start = 1 << (half - 1)
  pref_val = 0
  prefix.each_char { |c| pref_val = (pref_val << 1) | (c.ord - 48) }
  ans += pref_val - start
  pal = prefix.dup
  (half - 1 - (l % 2)).downto(0) { |i| pal += prefix[i] }
  pval = 0
  pal.each_char { |c| pval = (pval << 1) | (c.ord - 48) }
  ans += 1 if pval <= n
  ans
end
