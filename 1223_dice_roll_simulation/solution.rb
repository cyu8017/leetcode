# LeetCode 1223 - Dice Roll Simulation
# https://leetcode.com/problems/dice-roll-simulation/

# @param {Integer} n
# @param {Integer[]} roll_max
# @return {Integer}
def die_simulator(n, roll_max)
  mod = 1_000_000_007
  dp = Array.new(6) { |j| Array.new(roll_max[j] + 1, 0) }
  6.times { |j| dp[j][1] = 1 }
  (1...n).each do
    totals = dp.map { |row| row.sum % mod }
    nxt = Array.new(6) { |j| Array.new(dp[j].length, 0) }
    6.times do |j|
      nxt[j][1] = (totals.sum - totals[j]) % mod
      (2...dp[j].length).each { |run| nxt[j][run] = dp[j][run - 1] }
    end
    dp = nxt
  end
  dp.sum { |row| row.sum } % mod
end
