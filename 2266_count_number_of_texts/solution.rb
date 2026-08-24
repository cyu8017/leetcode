# LeetCode 2266 - Count Number of Texts
# https://leetcode.com/problems/count-number-of-texts/

# @param {String} pressed_keys
# @return {Integer}
def count_texts(pressed_keys)
  mod = 1_000_000_007
  n = pressed_keys.length
  dp = Array.new(n + 1, 0)
  dp[0] = 1
  (1..n).each do |i|
    dp[i] = dp[i - 1]
    max_press = %w[7 9].include?(pressed_keys[i - 1]) ? 4 : 3
    (2..max_press).each do |j|
      break if j > i
      break if pressed_keys[i - j] != pressed_keys[i - 1]

      dp[i] = (dp[i] + dp[i - j]) % mod
    end
  end
  dp[n]
end
