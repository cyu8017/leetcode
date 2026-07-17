# LeetCode 1763 - Longest Nice Substring
# https://leetcode.com/problems/longest-nice-substring/

# @param {String} s
# @return {String}
def longest_nice_substring(s)
  best_start = 0
  best_len = 0
  (0...s.length).each do |i|
    lower = 0
    upper = 0
    (i...s.length).each do |j|
      code = s[j].ord
      if code >= 97
        lower |= 1 << (code - 97)
      else
        upper |= 1 << (code - 65)
      end
      if lower == upper && j - i + 1 > best_len
        best_start = i
        best_len = j - i + 1
      end
    end
  end
  s[best_start, best_len]
end
