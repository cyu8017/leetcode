# LeetCode 3019 - Number of Changing Keys
# https://leetcode.com/problems/number-of-changing-keys/

# @param {String} s
# @return {Integer}
def count_key_changes(s)
  s = s.downcase
  ans = 0
  (1...s.length).each { |i| ans += 1 if s[i] != s[i - 1] }
  ans
end
