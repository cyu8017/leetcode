# LeetCode 2466 - Count Ways To Build Good Strings
# https://leetcode.com/problems/count-ways-to-build-good-strings/

# @param {Integer} low
# @param {Integer} high
# @param {Integer} zero
# @param {Integer} one
# @return {Integer}
def count_good_strings(low, high, zero, one)
  mod = 1_000_000_007
  dp = Array.new(high + 1, 0)
  dp[0] = 1
  ans = 0
  (1..high).each do |i|
    dp[i] = (dp[i] + dp[i - zero]) % mod if i >= zero
    dp[i] = (dp[i] + dp[i - one]) % mod if i >= one
    ans = (ans + dp[i]) % mod if i >= low
  end
  ans
end
