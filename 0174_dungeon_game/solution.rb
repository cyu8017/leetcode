# LeetCode 0174 - Dungeon Game
# https://leetcode.com/problems/dungeon-game/

class Solution
  def calculate_minimum_hp(dungeon)
    rows = dungeon.length
    cols = dungeon[0].length
    dp = Array.new(rows + 1) { Array.new(cols + 1, Float::INFINITY) }
    dp[rows][cols - 1] = 1
    dp[rows - 1][cols] = 1

    (rows - 1).downto(0) do |row|
      (cols - 1).downto(0) do |col|
        need = [dp[row + 1][col], dp[row][col + 1]].min - dungeon[row][col]
        dp[row][col] = [1, need].max
      end
    end
    dp[0][0]
  end
end