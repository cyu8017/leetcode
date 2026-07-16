# LeetCode 0526 - Beautiful Arrangement
# https://leetcode.com/problems/beautiful-arrangement/

require "set"

class Solution
  def count_arrangement(n)
    @count = 0
    backtrack(1, Set.new, n)
    @count
  end

  alias_method :countArrangement, :count_arrangement

  private

  def backtrack(index, used, n)
    if index == n + 1
      @count += 1
      return
    end
    (1..n).each do |num|
      next if used.include?(num)
      next unless index % num == 0 || num % index == 0

      used.add(num)
      backtrack(index + 1, used, n)
      used.delete(num)
    end
  end
end
