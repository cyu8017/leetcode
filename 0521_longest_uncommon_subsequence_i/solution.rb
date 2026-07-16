# LeetCode 0521 - Longest Uncommon Subsequence I
# https://leetcode.com/problems/longest-uncommon-subsequence-i/

class Solution
  def find_luslength(a, b)
    a != b ? [a.length, b.length].max : -1
  end

  alias_method :findLUSlength, :find_luslength
end
