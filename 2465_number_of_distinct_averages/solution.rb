# LeetCode 2465 - Number of Distinct Averages
# https://leetcode.com/problems/number-of-distinct-averages/

# @param {Integer[]} nums
# @return {Integer}
def distinct_averages(nums)
  nums = nums.sort
  seen = {}
  l = 0
  r = nums.length - 1
  while l < r
    seen[nums[l] + nums[r]] = true
    l += 1
    r -= 1
  end
  seen.length
end
