# LeetCode 1561 - Maximum Number of Coins You Can Get
# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

# @param {Integer[]} piles
# @return {Integer}
def max_coins(piles)
  piles = piles.sort
  piles[(piles.length / 3)..].each_slice(2).sum(&:first)
end
