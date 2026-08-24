# LeetCode 2002 - Maximum Product of the Length of Two Palindromic Subsequences
# https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/

# @param {String} s
# @return {Integer}
def max_product(s)
  pal_len = lambda do |mask|
    chars = []
    s.each_char.with_index { |ch, i| chars << ch if (mask & (1 << i)) != 0 }
    l = 0
    r = chars.length - 1
    while l < r
      return 0 if chars[l] != chars[r]

      l += 1
      r -= 1
    end
    chars.length
  end
  n = s.length
  best = 0
  total = 1 << n
  (1...total).each do |mask1|
    len1 = pal_len.call(mask1)
    next if len1.zero?

    remain = (total - 1) ^ mask1
    mask2 = remain
    while mask2 > 0
      len2 = pal_len.call(mask2)
      best = len1 * len2 if len2.positive? && len1 * len2 > best
      mask2 = (mask2 - 1) & remain
    end
  end
  best
end
