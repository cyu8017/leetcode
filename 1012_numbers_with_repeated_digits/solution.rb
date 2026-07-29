# LeetCode 1012 - Numbers With Repeated Digits
# https://leetcode.com/problems/numbers-with-repeated-digits/

# @param {Integer} n
# @return {Integer}
def num_dup_digits_at_most_n(n)
  digits = n.to_s.chars.map(&:to_i)
  m = digits.length

  perm = lambda do |a, b|
    res = 1
    b.times { |i| res *= a - i }
    res
  end

  total_unique = 0
  (1...m).each { |length| total_unique += 9 * perm.call(9, length - 1) }

  used = {}
  broken = false
  digits.each_with_index do |d, i|
    ((i.zero? ? 1 : 0)...d).each do |x|
      next if used[x]

      total_unique += perm.call(9 - i, m - i - 1)
    end
    if used[d]
      broken = true
      break
    end
    used[d] = true
  end
  total_unique += 1 unless broken
  n - total_unique
end
