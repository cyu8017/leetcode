# LeetCode 2952 - Minimum Number of Coins to be Added
# https://leetcode.com/problems/minimum-number-of-coins-to-be-added/

# @param {Integer[]} coins
# @param {Integer} target
# @return {Integer}
def minimum_added_coins(coins, target)
  coins.sort!
  ans = 0
  reach = 0
  i = 0
  while reach < target
    if i < coins.length && coins[i] <= reach + 1
      reach += coins[i]
      i += 1
    else
      reach += reach + 1
      ans += 1
    end
  end
  ans
end
