# LeetCode 0386 - Lexicographical Numbers
# https://leetcode.com/problems/lexicographical-numbers/

class Solution
  def lexical_order(n)
    result = []

    dfs = lambda do |current|
      return if current > n

      result << current
      dfs.call(current * 10)
      dfs.call(current + 1) if current % 10 < 9
    end

    dfs.call(1)
    result
  end

  alias_method :lexicalOrder, :lexical_order
end
