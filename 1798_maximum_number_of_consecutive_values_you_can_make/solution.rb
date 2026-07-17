# LeetCode 1798 - Maximum Number of Consecutive Values You Can Make
# https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/

# @param {Integer[]} coins
# @return {Integer}
def get_maximum_consecutive(coins)
  reach = 0
  coins.sort.each do |coin|
    break if coin > reach + 1
    reach += coin
  end
  reach + 1
end
