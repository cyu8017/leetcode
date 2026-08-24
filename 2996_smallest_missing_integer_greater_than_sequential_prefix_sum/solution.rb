# LeetCode 2996 - Smallest Missing Integer Greater Than Sequential Prefix Sum
# https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/

# @param {Integer[]} nums
# @return {Integer}
def missing_integer(nums)
  total = nums[0]
  i = 1
  while i < nums.length && nums[i] == nums[i - 1] + 1
    total += nums[i]
    i += 1
  end
  seen = {}
  nums.each { |v| seen[v] = true }
  total += 1 while seen[total]
  total
end
