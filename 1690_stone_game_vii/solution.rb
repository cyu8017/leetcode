# LeetCode 1690 - Stone Game VII
# https://leetcode.com/problems/stone-game-vii/

# @param {Integer[]} stones
# @return {Integer}
def stone_game_v_i_i(stones)
  n = stones.length
  pre = [0]
  stones.each { |x| pre << pre[-1] + x }
  dp = Array.new(n) { Array.new(n, 0) }
  (2..n).each do |length|
    (0..(n - length)).each do |i|
      j = i + length - 1
      dp[i][j] = [
        pre[j + 1] - pre[i + 1] - dp[i + 1][j],
        pre[j] - pre[i] - dp[i][j - 1]
      ].max
    end
  end
  dp[0][n - 1]
end
