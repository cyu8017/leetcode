# LeetCode 1406 - Stone Game Iii
# https://leetcode.com/problems/stone-game-iii/

def stone_game_iii(stone_value)
  n = stone_value.length
  dp = Array.new(n + 1, 0)
  (n - 1).downto(0) do |i|
    take = 0
    dp[i] = -10**18
    (i...[i + 3, n].min).each do |j|
      take += stone_value[j]
      dp[i] = [dp[i], take - dp[j + 1]].max
    end
  end
  dp[0] > 0 ? 'Alice' : (dp[0] < 0 ? 'Bob' : 'Tie')
end
