# LeetCode 0906 - Super Palindromes
# https://leetcode.com/problems/super-palindromes/

# @param {String} left
# @param {String} right
# @return {Integer}
def superpalindromes_in_range(left, right)
  l = left.to_i
  r = right.to_i

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

  valid_root = lambda do |pal, odd_root|
    if odd_root && pal.to_s.length == 1
      return [2, 3, 5].include?(pal)
    end

    is_prime.call(pal)
  end

  ans = 0
  ans += 1 if l <= 1 && 1 <= r
  (1..(10**5)).each do |k|
    s = k.to_s
    pal = (s + s.reverse).to_i
    sq = pal * pal
    break if sq > r

    ans += 1 if sq >= l && valid_root.call(pal, false)
  end
  (1..(10**5)).each do |k|
    s = k.to_s
    pal = (s + s[0...-1].reverse).to_i
    sq = pal * pal
    break if sq > r

    ans += 1 if sq >= l && valid_root.call(pal, true)
  end
  ans
end
