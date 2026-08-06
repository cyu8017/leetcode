# LeetCode 1999 - Smallest Greater Multiple Made of Two Digits
# https://leetcode.com/problems/smallest-greater-multiple-made-of-two-digits/

# @param {Integer} k
# @param {Integer} digit1
# @param {Integer} digit2
# @return {Integer}
def find_integer(k, digit1, digit2)
  digits = [digit1, digit2].uniq.sort
  q = []
  digits.each { |d| q << d unless d.zero? }
  return -1 if q.empty?
  seen = q.to_h { |x| [x, true] }
  until q.empty?
    x = q.shift
    return x if x > k && (x % k).zero?
    digits.each do |d|
      nx = x * 10 + d
      next if nx > 2**31 - 1 || seen[nx]
      seen[nx] = true
      q << nx
    end
  end
  -1
end
