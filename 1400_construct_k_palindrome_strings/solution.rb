# LeetCode 1400 - Construct K Palindrome Strings
# https://leetcode.com/problems/construct-k-palindrome-strings/

def can_construct(s, k)
  counts = Hash.new(0)
  s.each_char { |ch| counts[ch] += 1 }
  odds = counts.values.count(&:odd?)
  odds <= k && k <= s.length
end
