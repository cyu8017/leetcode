# LeetCode 1262 - Greatest Sum Divisible by Three
# https://leetcode.com/problems/greatest-sum-divisible-by-three/

# @param {Integer[]} nums
# @return {Integer}
def max_sum_div_three(nums)
  impossible = -10**18
  dp = [0, impossible, impossible]
  nums.each do |value|
    old = dp.dup
    old.each do |total|
      next if total == impossible
      remainder = (total + value) % 3
      dp[remainder] = [dp[remainder], total + value].max
    end
  end
  dp[0]
end
