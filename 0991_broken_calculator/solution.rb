# LeetCode 0991 - Broken Calculator
# https://leetcode.com/problems/broken-calculator/

# @param {Integer} start_value
# @param {Integer} target
# @return {Integer}
def broken_calc(start_value, target)
  ans = 0
  while target > start_value
    if target.odd?
      target += 1
    else
      target /= 2
    end
    ans += 1
  end
  ans + start_value - target
end
