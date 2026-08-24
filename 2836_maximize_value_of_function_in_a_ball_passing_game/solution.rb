# LeetCode 2836 - Maximize Value of Function in a Ball Passing Game
# https://leetcode.com/problems/maximize-value-of-function-in-a-ball-passing-game/

# @param {Integer[]} receiver
# @param {Integer} k
# @return {Integer}
def get_max_function_value(receiver, k)
  n = receiver.length
  log = 36
  up = Array.new(log) { Array.new(n, 0) }
  sm = Array.new(log) { Array.new(n, 0) }
  (0...n).each do |i|
    up[0][i] = receiver[i]
    sm[0][i] = receiver[i]
  end
  (1...log).each do |j|
    (0...n).each do |i|
      mid = up[j - 1][i]
      up[j][i] = up[j - 1][mid]
      sm[j][i] = sm[j - 1][i] + sm[j - 1][mid]
    end
  end
  ans = 0
  (0...n).each do |i|
    cur = i
    total = i
    kk = k
    (0...log).each do |j|
      if (kk & (1 << j)) != 0
        total += sm[j][cur]
        cur = up[j][cur]
      end
    end
    ans = total if total > ans
  end
  ans
end
