# LeetCode 1269 - Number of Ways to Stay in the Same Place After Some Steps
# https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/

# @param {Integer} steps
# @param {Integer} arr_len
# @return {Integer}
def num_ways(steps, arr_len)
  mod = 1_000_000_007
  width = [arr_len, steps / 2 + 1].min
  dp = [1] + [0] * (width - 1)
  steps.times do
    dp = width.times.map do |i|
      (dp[i] + (i > 0 ? dp[i - 1] : 0) + (i + 1 < width ? dp[i + 1] : 0)) % mod
    end
  end
  dp[0]
end
