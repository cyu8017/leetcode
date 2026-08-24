# LeetCode 2327 - Number of People Aware of a Secret
# https://leetcode.com/problems/number-of-people-aware-of-a-secret/

# @param {Integer} n
# @param {Integer} delay
# @param {Integer} forget
# @return {Integer}
def people_aware_of_secret(n, delay, forget)
  mod = 1_000_000_007
  dp = Array.new(n + 1, 0)
  dp[1] = 1
  share = 0
  (2..n).each do |day|
    share = (share + dp[day - delay]) % mod if day - delay >= 1
    share = (share - dp[day - forget] + mod) % mod if day - forget >= 1
    dp[day] = share
  end
  ans = 0
  ((n - forget + 1)..n).each do |day|
    ans = (ans + dp[day]) % mod if day >= 1
  end
  ans
end
