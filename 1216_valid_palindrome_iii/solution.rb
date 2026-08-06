# LeetCode 1216 - Valid Palindrome III
# https://leetcode.com/problems/valid-palindrome-iii/

# @param {String} s
# @param {Integer} k
# @return {Boolean}
def is_valid_palindrome(s, k)
  dp = Array.new(s.length, 0)
  (s.length - 1).downto(0) do |i|
    previous = 0
    ((i + 1)...s.length).each do |j|
      old = dp[j]
      dp[j] = s[i] == s[j] ? previous : 1 + [dp[j], dp[j - 1]].min
      previous = old
    end
  end
  s.empty? || dp[-1] <= k
end
