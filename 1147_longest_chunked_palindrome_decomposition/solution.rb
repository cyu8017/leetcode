# LeetCode 1147 - Longest Chunked Palindrome Decomposition
# https://leetcode.com/problems/longest-chunked-palindrome-decomposition/

# @param {String} text
# @return {Integer}
def longest_decomposition(text)
  n = text.length
  ans = 0
  i = 0
  while i < n - i
    found = false
    (1..((n - 2 * i) / 2)).each do |length|
      if text[i, length] == text[n - i - length, length]
        ans += 2
        i += length
        found = true
        break
      end
    end
    unless found
      ans += 1
      break
    end
  end
  ans
end
