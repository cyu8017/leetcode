# LeetCode 1347 - Minimum Number Of Steps To Make Two Strings Anagram
# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

def min_steps(s, t)
  counts = Hash.new(0)
  s.each_char { |c| counts[c] += 1 }
  t.each_char { |c| counts[c] -= 1 }
  counts.values.select(&:positive?).sum
end
