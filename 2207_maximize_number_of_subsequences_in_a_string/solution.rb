# LeetCode 2207 - Maximize Number of Subsequences in a String
# https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/

# @param {String} text
# @param {String} pattern
# @return {Integer}
def maximum_subsequence_count(text, pattern)
  a = pattern[0]
  b = pattern[1]
  count = lambda do |s|
    ca = 0
    ans = 0
    s.each_char do |ch|
      ans += ca if ch == b
      ca += 1 if ch == a
    end
    ans
  end
  [count.call(a + text), count.call(text + b)].max
end
