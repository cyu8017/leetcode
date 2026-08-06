# LeetCode 1550 - Three Consecutive Odds
# https://leetcode.com/problems/three-consecutive-odds/

# @param {Integer[]} arr
# @return {Boolean}
def three_consecutive_odds(arr)
  run = 0
  arr.each do |value|
    run = value.odd? ? run + 1 : 0
    return true if run == 3
  end
  false
end
