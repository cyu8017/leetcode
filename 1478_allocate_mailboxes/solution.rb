# LeetCode 1478 - Allocate Mailboxes
# https://leetcode.com/problems/allocate-mailboxes/

def min_distance(houses, k)
  houses.sort!
  n = houses.length
  cost = Array.new(n) { Array.new(n, 0) }
  n.times do |i|
    (i...n).each do |j|
      mid = houses[(i + j) / 2]
      cost[i][j] = (i..j).sum { |t| (houses[t] - mid).abs }
    end
  end
  dp = [0] + Array.new(n, 10**15)
  k.times do
    ndp = [0] + Array.new(n, 10**15)
    (1..n).each do |j|
      ndp[j] = (0...j).map { |i| dp[i] + cost[i][j - 1] }.min
    end
    dp = ndp
  end
  dp[n]
end
