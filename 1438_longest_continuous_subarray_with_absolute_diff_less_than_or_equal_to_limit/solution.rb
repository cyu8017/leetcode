# LeetCode 1438 - Longest Continuous Subarray With Absolute Diff Less Than Or Equal To Limit
# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

def longest_subarray(nums, limit)
  low = []
  high = []
  left = answer = 0
  nums.each_with_index do |value, right|
    low.pop while !low.empty? && nums[low[-1]] > value
    high.pop while !high.empty? && nums[high[-1]] < value
    low << right
    high << right
    while nums[high[0]] - nums[low[0]] > limit
      left += 1
      low.shift if low[0] < left
      high.shift if high[0] < left
    end
    answer = [answer, right - left + 1].max
  end
  answer
end
