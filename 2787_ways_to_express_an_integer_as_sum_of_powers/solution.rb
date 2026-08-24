# LeetCode 2787 - Ways to Express an Integer as Sum of Powers
# https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/

# @param {Integer} n
# @param {Integer} x
# @return {Integer}
def number_of_ways(n, x)
  mod = 1_000_000_007
  powers = []
  i = 1
  loop do
    p = 1
    x.times do
      p *= i
      break if p > n
    end
    break if p > n
    powers << p
    i += 1
  end
  dp = Array.new(n + 1, 0)
  dp[0] = 1
  powers.each do |pw|
    n.downto(pw) { |s| dp[s] = (dp[s] + dp[s - pw]) % mod }
  end
  dp[n]
end
