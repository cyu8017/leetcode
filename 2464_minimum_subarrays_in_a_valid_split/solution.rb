# LeetCode 2464 - Minimum Subarrays in a Valid Split
# https://leetcode.com/problems/minimum-subarrays-in-a-valid-split/

# @param {Integer[]} nums
# @return {Integer}
def valid_subarray_split(nums)
  gcd = lambda do |a, b|
    while b != 0
      a, b = b, a % b
    end
    a
  end

  n = nums.length
  inf = 1 << 30
  dp = Array.new(n + 1, inf)
  dp[0] = 0
  (0...n).each do |i|
    next if dp[i] >= inf

    (i...n).each do |j|
      dp[j + 1] = dp[i] + 1 if gcd.call(nums[i], nums[j]) > 1 && dp[i] + 1 < dp[j + 1]
    end
  end
  dp[n] >= inf ? -1 : dp[n]
end
