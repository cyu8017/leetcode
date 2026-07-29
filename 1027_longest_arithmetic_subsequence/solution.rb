# LeetCode 1027 - Longest Arithmetic Subsequence
# https://leetcode.com/problems/longest-arithmetic-subsequence/

# @param {Integer[]} nums
# @return {Integer}
def longest_arith_seq_length(nums)
  dp = Array.new(nums.length) { {} }
  ans = 1
  (1...nums.length).each do |j|
    (0...j).each do |i|
      d = nums[j] - nums[i]
      dp[j][d] = (dp[i][d] || 1) + 1
      ans = [ans, dp[j][d]].max
    end
  end
  ans
end
