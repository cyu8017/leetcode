# LeetCode 3260 - Find the Largest Palindrome Divisible by K
# https://leetcode.com/problems/find-the-largest-palindrome-divisible-by-k/

# @param {Integer} n
# @param {Integer} k
# @return {String}
def largest_palindrome(n, k)
  digits = Array.new(n, "9")
  half = (n + 1) / 2
  mod7 = lambda do |s|
    r = 0
    s.each_char { |ch| r = (r * 10 + (ch.ord - 48)) % 7 }
    r
  end
  largest_pal7 = lambda do |nn|
    half_len = (nn + 1) / 2
    half_d = Array.new(half_len, "9")
    loop do
      pal = Array.new(nn, "")
      (0...half_len).each { |i| pal[i] = half_d[i] }
      (0...(nn / 2)).each { |i| pal[nn - 1 - i] = pal[i] }
      return pal.join if mod7.call(pal.join) == 0
      idx = half_len - 1
      while idx >= 0 && half_d[idx] == "0"
        half_d[idx] = "9"
        idx -= 1
      end
      break if idx < 0
      half_d[idx] = (half_d[idx].ord - 1).chr
    end
    ""
  end
  return digits.join if [1, 3, 9].include?(k)
  if k == 2
    digits[0] = digits[n - 1] = "8"
    return digits.join
  end
  if k == 4
    return "8" if n == 1
    digits[0] = digits[1] = digits[n - 1] = digits[n - 2] = "8"
    return digits.join
  end
  if k == 5
    digits[0] = digits[n - 1] = "5"
    return digits.join
  end
  if k == 8
    return Array.new(n, "8").join if n <= 2
    digits[0] = digits[1] = digits[2] = "8"
    digits[n - 1] = digits[n - 2] = digits[n - 3] = "8"
    return digits.join
  end
  if k == 6
    return "6" if n == 1
    digits[0] = digits[n - 1] = "8"
    ssum = 16 + 9 * (n - 2)
    need = ssum % 3
    if need != 0
      pos = half - 1
      digits[pos] = (digits[pos].ord - need).chr
      digits[n - 1 - pos] = digits[pos] if n.even? || pos != n - 1 - pos
    end
    return digits.join
  end
  return largest_pal7.call(n) if k == 7
  digits.join
end
