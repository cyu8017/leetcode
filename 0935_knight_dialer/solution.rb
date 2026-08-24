# LeetCode 0935 - Knight Dialer
# https://leetcode.com/problems/knight-dialer/

# @param {Integer} n
# @return {Integer}
def knight_dialer(n)
  mod = 10**9 + 7
  moves = {
    0 => [4, 6],
    1 => [6, 8],
    2 => [7, 9],
    3 => [4, 8],
    4 => [0, 3, 9],
    5 => [],
    6 => [0, 1, 7],
    7 => [2, 6],
    8 => [1, 3],
    9 => [2, 4]
  }
  dp = Array.new(10, 1)
  (n - 1).times do
    ndp = Array.new(10, 0)
    10.times do |i|
      moves[i].each { |j| ndp[j] = (ndp[j] + dp[i]) % mod }
    end
    dp = ndp
  end
  dp.sum % mod
end
