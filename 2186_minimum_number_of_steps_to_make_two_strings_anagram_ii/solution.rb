# LeetCode 2186 - Minimum Number of Steps to Make Two Strings Anagram II
# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/

# @param {String} s
# @param {String} t
# @return {Integer}
def min_steps(s, t)
  freq = Array.new(26, 0)
  s.each_byte { |b| freq[b - 97] += 1 }
  t.each_byte { |b| freq[b - 97] -= 1 }
  freq.sum(&:abs)
end
