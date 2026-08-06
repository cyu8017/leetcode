# LeetCode 1523 - Count Odd Numbers in an Interval Range
# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

# @param {Integer} low
# @param {Integer} high
# @return {Integer}
def count_odds(low, high)
  (high + 1) / 2 - low / 2
end
