# LeetCode 2915 - Length of the Longest Subsequence That Sums to Target
# https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def length_of_longest_subsequence(nums, target)
  dp = Array.new(target + 1, -1)
  dp[0] = 0
  nums.each do |v|
    target.downto(v) do |s|
      dp[s] = dp[s - v] + 1 if dp[s - v] >= 0 && dp[s - v] + 1 > dp[s]
    end
  end
  dp[target]
end
