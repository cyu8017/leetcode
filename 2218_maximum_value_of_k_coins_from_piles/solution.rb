# LeetCode 2218 - Maximum Value of K Coins From Piles
# https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/

# @param {Integer[][]} piles
# @param {Integer} k
# @return {Integer}
def max_value_of_coins(piles, k)
  dp = Array.new(k + 1, 0)
  piles.each do |pile|
    ndp = dp.dup
    sum = 0
    take = 1
    while take <= pile.length && take <= k
      sum += pile[take - 1]
      (take..k).each do |j|
        ndp[j] = [ndp[j], dp[j - take] + sum].max
      end
      take += 1
    end
    dp = ndp
  end
  dp[k]
end
