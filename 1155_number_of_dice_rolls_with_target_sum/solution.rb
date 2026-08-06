# LeetCode 1155 - Number of Dice Rolls With Target Sum
# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

# @param {Integer} n
# @param {Integer} k
# @param {Integer} target
# @return {Integer}
def num_rolls_to_target(n, k, target)
  mod = 10**9 + 7
  dp = Array.new(target + 1, 0)
  dp[0] = 1
  n.times do
    new_dp = Array.new(target + 1, 0)
    (0..target).each do |s|
      next if dp[s].zero?
      (1..k).each do |face|
        new_dp[s + face] = (new_dp[s + face] + dp[s]) % mod if s + face <= target
      end
    end
    dp = new_dp
  end
  dp[target]
end
