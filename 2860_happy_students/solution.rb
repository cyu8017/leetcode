# LeetCode 2860 - Happy Students
# https://leetcode.com/problems/happy-students/

# @param {Integer[]} nums
# @return {Integer}
def count_ways(nums)
  nums = nums.sort
  n = nums.length
  ans = 0
  ans += 1 if nums[0] > 0
  (0...n).each do |i|
    selected = i + 1
    ans += 1 if selected > nums[i] && (i == n - 1 || selected < nums[i + 1])
  end
  ans
end
