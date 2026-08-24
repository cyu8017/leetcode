# LeetCode 3413 - Maximum Coins From K Consecutive Bags
# https://leetcode.com/problems/maximum-coins-from-k-consecutive-bags/

# @param {Integer[][]} coins
# @param {Integer} k
# @return {Integer}
def maximum_coins(coins, k)
  coins = coins.sort_by { |a| a[0] }
  ans = 0
  n = coins.length
  (0...n).each do |i|
    s = 0
    start = coins[i][0]
    last = start + k - 1
    j = i
    while j < n && coins[j][0] <= last
      l = coins[j][0]
      r = coins[j][1]
      r = last if r > last
      l = start if l < start
      s += (r - l + 1) * coins[j][2] if l <= r
      j += 1
    end
    ans = s if s > ans
  end
  (0...n).each do |i|
    s = 0
    last = coins[i][1]
    start = last - k + 1
    (0..i).each do |j|
      l = coins[j][0]
      r = coins[j][1]
      l = start if l < start
      r = last if r > last
      s += (r - l + 1) * coins[j][2] if l <= r
    end
    ans = s if s > ans
  end
  ans
end
