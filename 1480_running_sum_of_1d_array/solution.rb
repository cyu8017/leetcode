# LeetCode 1480 - Running Sum Of 1D Array
# https://leetcode.com/problems/running-sum-of-1d-array/

def running_sum(nums)
  (1...nums.length).each { |i| nums[i] += nums[i - 1] }
  nums
end
