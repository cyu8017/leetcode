# LeetCode 0459 - Repeated Substring Pattern
# https://leetcode.com/problems/repeated-substring-pattern/

class Solution
  def repeated_substring_pattern(s)
    doubled = s + s
    doubled[1...-1].include?(s)
  end

  alias_method :repeatedSubstringPattern, :repeated_substring_pattern
end
