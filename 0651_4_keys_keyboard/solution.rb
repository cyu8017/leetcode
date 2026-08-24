# LeetCode 0651 - 4 Keys Keyboard
# https://leetcode.com/problems/4-keys-keyboard/

# @param {Integer} n
# @return {Integer}
def max_a(n)
  dp = (0..n).to_a
  (1..n).each do |i|
    (0...(i - 2)).each do |j|
      dp[i] = [dp[i], dp[j] * (i - j - 1)].max
    end
  end
  dp[n]
end
