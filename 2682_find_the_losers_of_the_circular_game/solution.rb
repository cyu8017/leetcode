# LeetCode 2682 - Find the Losers of the Circular Game
# https://leetcode.com/problems/find-the-losers-of-the-circular-game/

# @param {Integer} n
# @param {Integer} k
# @return {Integer[]}
def circular_game_losers(n, k)
  seen = Array.new(n + 1, false)
  cur = 1
  step = 1
  until seen[cur]
    seen[cur] = true
    cur = (cur - 1 + step * k) % n + 1
    step += 1
  end
  (1..n).select { |i| !seen[i] }
end
