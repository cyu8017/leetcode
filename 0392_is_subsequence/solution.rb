# LeetCode 0392 - Is Subsequence
# https://leetcode.com/problems/is-subsequence/

class Solution
  def is_subsequence(s, t)
    index = 0
    t.each_char do |char|
      if index < s.length && s[index] == char
        index += 1
      end
    end
    index == s.length
  end

  alias_method :isSubsequence, :is_subsequence
end
