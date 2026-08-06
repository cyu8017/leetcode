# LeetCode 1259 - Handshakes That Don't Cross
# https://leetcode.com/problems/handshakes-that-dont-cross/

# @param {Integer} num_people
# @return {Integer}
def number_of_ways(num_people)
  mod = 1_000_000_007
  dp = Array.new(num_people + 1, 0)
  dp[0] = 1
  2.step(num_people, 2) do |people|
    dp[people] = (0...people).step(2).sum { |left| dp[left] * dp[people - 2 - left] } % mod
  end
  dp[num_people]
end
