# LeetCode 0520 - Detect Capital
# https://leetcode.com/problems/detect-capital/

class Solution
  def detect_capital_use(word)
    word == word.upcase || word == word.downcase || word == word.capitalize
  end

  alias_method :detectCapitalUse, :detect_capital_use
end
