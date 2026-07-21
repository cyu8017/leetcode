# LeetCode 1866 - Number of Ways to Rearrange Sticks With K Sticks Visible
# https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/

# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def rearrange_sticks(n, k)
  mod = 10**9 + 7
  return 0 if k == 0 || k > n

  dp = Array.new(n + 1) { Array.new(n + 1, 0) }
  dp[1][1] = 1
  (2..n).each do |sticks|
    dp[sticks][1] = (sticks - 1) * dp[sticks - 1][1] % mod
    (2..sticks).each do |visible|
      dp[sticks][visible] = (
        dp[sticks - 1][visible - 1] + (sticks - 1) * dp[sticks - 1][visible]
      ) % mod
    end
  end

  dp[n][k]
end
