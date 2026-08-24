# LeetCode 0866 - Prime Palindrome
# https://leetcode.com/problems/prime-palindrome/

# @param {Integer} n
# @return {Integer}
def prime_palindrome(n)
  is_prime = lambda do |x|
    return false if x < 2
    return x == 2 if x.even?

    d = 3
    while d * d <= x
      return false if x % d == 0

      d += 2
    end
    true
  end

  pals = lambda do
    (1..5).each do |length|
      start = 10**(length - 1)
      finish = 10**length
      (start...finish).each do |root|
        s = root.to_s
        pal = (s + s[0, [s.length - 1, 1].max].reverse).to_i
        return pal if pal >= n && is_prime.call(pal)
      end
    end
    0
  end

  return 2 if n <= 2
  return 3 if n <= 3
  return 5 if n <= 5
  return 7 if n <= 7
  return 11 if n <= 11

  pals.call
end
