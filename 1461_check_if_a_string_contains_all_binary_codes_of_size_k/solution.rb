# LeetCode 1461 - Check If A String Contains All Binary Codes Of Size K
# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

def has_all_codes(s, k)
  seen = {}
  (0..(s.length - k)).each { |i| seen[s[i, k]] = true }
  seen.length == (1 << k)
end
