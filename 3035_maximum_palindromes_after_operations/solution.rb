# LeetCode 3035 - Maximum Palindromes After Operations
# https://leetcode.com/problems/maximum-palindromes-after-operations/

# @param {String[]} words
# @return {Integer}
def max_palindromes_after_operations(words)
  s = 0
  mask = 0
  words.each do |w|
    s += w.length
    w.each_char { |ch| mask ^= 1 << (ch.ord - 97) }
  end
  s -= popcount(mask)
  words.sort_by!(&:length)
  ans = 0
  words.each do |w|
    s -= (w.length / 2) * 2
    break if s < 0

    ans += 1
  end
  ans
end

def popcount(x)
  c = 0
  while x != 0
    c += x & 1
    x >>= 1
  end
  c
end
