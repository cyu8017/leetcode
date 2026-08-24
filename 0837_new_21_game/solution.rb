# LeetCode 0837 - New 21 Game
# https://leetcode.com/problems/new-21-game/

# @param {Integer} n
# @param {Integer} k
# @param {Integer} max_pts
# @return {Float}
def new21_game(n, k, max_pts)
  return 1.0 if k == 0 || n >= k - 1 + max_pts

  dp = Array.new(n + 1, 0.0)
  dp[0] = 1.0
  window = 1.0
  ans = 0.0
  (1..n).each do |i|
    dp[i] = window / max_pts
    if i < k
      window += dp[i]
    else
      ans += dp[i]
    end
    window -= dp[i - max_pts] if i - max_pts >= 0 && i - max_pts < k
  end
  ans
end
