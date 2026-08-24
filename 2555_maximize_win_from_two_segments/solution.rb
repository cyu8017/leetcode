# LeetCode 2555 - Maximize Win From Two Segments
# https://leetcode.com/problems/maximize-win-from-two-segments/

# @param {Integer[]} prize_positions
# @param {Integer} k
# @return {Integer}
def maximize_win(prize_positions, k)
  n = prize_positions.length
  dp = Array.new(n + 1, 0)
  ans = 0
  left = 0
  n.times do |right|
    left += 1 while prize_positions[right] - prize_positions[left] > k
    cur = right - left + 1
    ans = dp[left] + cur if dp[left] + cur > ans
    best = cur
    best = dp[right] if dp[right] > best
    dp[right + 1] = best
  end
  ans
end
