# LeetCode 0553 - Optimal Division
# https://leetcode.com/problems/optimal-division/

# @param {Integer[]} nums
# @return {String}
def optimal_division(nums)
  return nums[0].to_s if nums.length == 1
  return "#{nums[0]}/#{nums[1]}" if nums.length == 2

  "#{nums[0]}/(#{nums[1..].join('/')})"
end
