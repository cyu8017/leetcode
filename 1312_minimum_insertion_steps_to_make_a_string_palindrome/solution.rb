# LeetCode 1312 - Minimum Insertion Steps To Make A String Palindrome
# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

def min_insertions(s)
  n = s.length
  dp = Array.new(n, 0)
  (n - 2).downto(0) do |left|
    diagonal = 0
    ((left + 1)...n).each do |right|
      old = dp[right]
      dp[right] = if s[left] == s[right]
                    diagonal
                  else
                    1 + [dp[right], dp[right - 1]].min
                  end
      diagonal = old
    end
  end
  dp.empty? ? 0 : dp[-1]
end
