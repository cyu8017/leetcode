# LeetCode 2843 - Count Symmetric Integers
# https://leetcode.com/problems/count-symmetric-integers/

# @param {Integer} low
# @param {Integer} high
# @return {Integer}
def count_symmetric_integers(low, high)
  ans = 0
  (low..high).each do |x|
    s = x.to_s
    next if s.length.odd?

    mid = s.length / 2
    a = b = 0
    (0...mid).each do |i|
      a += s[i].ord - 48
      b += s[mid + i].ord - 48
    end
    ans += 1 if a == b
  end
  ans
end
