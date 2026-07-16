# LeetCode 0487 - Max Consecutive Ones II
# https://leetcode.com/problems/max-consecutive-ones-ii/

class Solution
  def find_max_consecutive_ones(nums)
    left = 0
    best = 0
    zeros = 0
    nums.each_with_index do |num, right|
      zeros += 1 if num == 0
      while zeros > 1
        zeros -= 1 if nums[left] == 0
        left += 1
      end
      best = [best, right - left + 1].max
    end
    best
  end

  alias_method :findMaxConsecutiveOnes, :find_max_consecutive_ones
end
