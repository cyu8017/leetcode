# LeetCode 1984 - Minimum Difference Between Highest and Lowest of K Scores
# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def minimum_difference(nums, k)
  nums = nums.sort
  (0..(nums.length - k)).map { |i| nums[i + k - 1] - nums[i] }.min
end
