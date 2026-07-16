# LeetCode 0228 - Summary Ranges
# https://leetcode.com/problems/summary-ranges/

# @param {Integer[]} nums
# @return {String[]}
def summary_ranges(nums)
  result = []
  index = 0

  while index < nums.length
    start = nums[index]
    while index + 1 < nums.length && nums[index + 1] == nums[index] + 1
      index += 1
    end
    if start == nums[index]
      result << start.to_s
    else
      result << "#{start}->#{nums[index]}"
    end
    index += 1
  end

  result
end
