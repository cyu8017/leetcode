# LeetCode 0485 - Max Consecutive Ones
# https://leetcode.com/problems/max-consecutive-ones/

class Solution
  def find_max_consecutive_ones(nums)
    best = 0
    current = 0
    nums.each do |num|
      if num == 1
        current += 1
        best = [best, current].max
      else
        current = 0
      end
    end
    best
  end

  alias_method :findMaxConsecutiveOnes, :find_max_consecutive_ones
end
