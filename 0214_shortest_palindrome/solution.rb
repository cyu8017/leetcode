# LeetCode 0214 - Shortest Palindrome
# https://leetcode.com/problems/shortest-palindrome/

class Solution
  def shortest_palindrome(s)
    return "" if s.empty?

    reversed_s = s.reverse
    combined = "#{s}##{reversed_s}"
    pi = Array.new(combined.length, 0)
    lps = 0
    (1...combined.length).each do |i|
      while lps.positive? && combined[i] != combined[lps]
        lps = pi[lps - 1]
      end
      lps += 1 if combined[i] == combined[lps]
      pi[i] = lps
    end
    prefix_len = pi[-1]
    "#{reversed_s[0, s.length - prefix_len]}#{s}"
  end
end
