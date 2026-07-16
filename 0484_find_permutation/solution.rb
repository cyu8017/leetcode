# LeetCode 0484 - Find Permutation
# https://leetcode.com/problems/find-permutation/

class Solution
  def find_permutation(s)
    stack = [1]
    result = []
    s.each_char do |ch|
      if ch == "I"
        until stack.empty?
          result << stack.pop
        end
      end
      stack << stack.length + result.length + 1
    end
    until stack.empty?
      result << stack.pop
    end
    result
  end

  alias_method :findPermutation, :find_permutation
end
