# LeetCode 2168 - Unique Substrings With Equal Digit Frequency
# https://leetcode.com/problems/unique-substrings-with-equal-digit-frequency/

# @param {String} s
# @return {Integer}
def equal_digit_frequency(s)
  n = s.length
  seen = {}
  n.times do |i|
    freq = Array.new(10, 0)
    maxf = 0
    kinds = 0
    (i...n).each do |j|
      d = s[j].ord - 48
      kinds += 1 if freq[d] == 0
      freq[d] += 1
      maxf = [maxf, freq[d]].max
      seen[s[i..j]] = true if maxf * kinds == j - i + 1
    end
  end
  seen.length
end
