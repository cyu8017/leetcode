# LeetCode 3303 - Find the Occurrence of First Almost Equal Substring
# https://leetcode.com/problems/find-the-occurrence-of-first-almost-equal-substring/

# @param {String} s
# @param {String} pattern
# @return {Integer}
def min_starting_index(s, pattern)
  n = s.length
  m = pattern.length
  (0..(n - m)).each do |i|
    diff = 0
    m.times do |j|
      if s[i + j] != pattern[j]
        diff += 1
        break if diff > 1
      end
    end
    return i if diff <= 1
  end
  -1
end
