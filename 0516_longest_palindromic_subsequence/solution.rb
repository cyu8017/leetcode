# LeetCode 0516 - Longest Palindromic Subsequence
# https://leetcode.com/problems/longest-palindromic-subsequence/

class Solution
  def longest_palindrome_subseq(s)
    length = s.length
    dp = Array.new(length) { Array.new(length, 0) }

    (length - 1).downto(0) do |index|
      dp[index][index] = 1
      ((index + 1)...length).each do |end_index|
        if s[index] == s[end_index]
          dp[index][end_index] = dp[index + 1][end_index - 1] + 2
        else
          dp[index][end_index] = [dp[index + 1][end_index], dp[index][end_index - 1]].max
        end
      end
    end

    dp[0][length - 1]
  end

  alias_method :longestPalindromeSubseq, :longest_palindrome_subseq
end
