# LeetCode 2533 - Number of Good Binary Strings
# https://leetcode.com/problems/number-of-good-binary-strings/

# @param {Integer} min_length
# @param {Integer} max_length
# @param {Integer} one_group
# @param {Integer} zero_group
# @return {Integer}
def good_binary_strings(min_length, max_length, one_group, zero_group)
  mod = 1_000_000_007
  dp = Array.new(max_length + 1, 0)
  dp[0] = 1
  (0..max_length).each do |i|
    next if dp[i] == 0

    dp[i + one_group] = (dp[i + one_group] + dp[i]) % mod if i + one_group <= max_length
    dp[i + zero_group] = (dp[i + zero_group] + dp[i]) % mod if i + zero_group <= max_length
  end
  ans = 0
  (min_length..max_length).each { |i| ans = (ans + dp[i]) % mod }
  ans
end

alias solve good_binary_strings
