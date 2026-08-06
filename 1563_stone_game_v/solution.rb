# LeetCode 1563 - Stone Game V
# https://leetcode.com/problems/stone-game-v/

# @param {Integer[]} stone_value
# @return {Integer}
def stone_game_v(stone_value)
  n = stone_value.length
  return 0 if n.zero?
  pre = [0]
  stone_value.each { |x| pre << pre[-1] + x }
  dp = Array.new(n) { Array.new(n, 0) }
  left = Array.new(n) { Array.new(n, 0) }
  right = Array.new(n) { Array.new(n, 0) }
  stone_value.each_with_index do |x, i|
    left[i][i] = right[i][i] = x
  end
  (2..n).each do |length|
    (0..(n - length)).each do |i|
      j = i + length - 1
      lo = i
      hi = j - 1
      while lo <= hi
        mid = (lo + hi) / 2
        if 2 * (pre[mid + 1] - pre[i]) >= pre[j + 1] - pre[i]
          hi = mid - 1
        else
          lo = mid + 1
        end
      end
      split = lo
      left_sum = pre[split + 1] - pre[i]
      right_sum = pre[j + 1] - pre[split + 1]
      best = right[split + 1][j]
      best = [best, left[i][split]].max if left_sum == right_sum
      best = [best, left[i][split - 1]].max if left_sum != right_sum && split > i
      dp[i][j] = best
      total = pre[j + 1] - pre[i]
      left[i][j] = [left[i][j - 1], total + best].max
      right[i][j] = [right[i + 1][j], total + best].max
    end
  end
  dp[0][n - 1]
end
