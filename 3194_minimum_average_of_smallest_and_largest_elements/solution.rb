# LeetCode 3194 - Minimum Average of Smallest and Largest Elements
# https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/

# @param {Integer[]} nums
# @return {Float}
def minimum_average(nums)
  nums.sort!
  n = nums.length
  ans = 1 << 30
  (0...(n / 2)).each { |i| ans = [ans, nums[i] + nums[n - i - 1]].min }
  ans / 2.0
end
