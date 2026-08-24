# LeetCode 2369 - Check if There is a Valid Partition For The Array
# https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/

# @param {Integer[]} nums
# @return {Boolean}
def valid_partition(nums)
  n = nums.length
  dp = Array.new(n + 1, false)
  dp[0] = true
  (1..n).each do |i|
    dp[i] = true if i >= 2 && nums[i - 1] == nums[i - 2] && dp[i - 2]
    dp[i] = true if i >= 3 && nums[i - 1] == nums[i - 2] && nums[i - 2] == nums[i - 3] && dp[i - 3]
    dp[i] = true if i >= 3 && nums[i - 1] == nums[i - 2] + 1 && nums[i - 2] == nums[i - 3] + 1 && dp[i - 3]
  end
  dp[n]
end
