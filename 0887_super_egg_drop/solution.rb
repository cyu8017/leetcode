# LeetCode 0887 - Super Egg Drop
# https://leetcode.com/problems/super-egg-drop/

# @param {Integer} k
# @param {Integer} n
# @return {Integer}
def super_egg_drop(k, n)
  dp = Array.new(k + 1, 0)
  moves = 0
  while dp[k] < n
    moves += 1
    k.downto(1) do |eggs|
      dp[eggs] = dp[eggs] + dp[eggs - 1] + 1
    end
  end
  moves
end
