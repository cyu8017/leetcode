# LeetCode 1176 - Diet Plan Performance
# https://leetcode.com/problems/diet-plan-performance/

# @param {Integer[]} calories
# @param {Integer} k
# @param {Integer} lower
# @param {Integer} upper
# @return {Integer}
def diet_plan_performance(calories, k, lower, upper)
  window = calories[0...k].sum
  ans = 0
  ans -= 1 if window < lower
  ans += 1 if window > upper
  (k...calories.length).each do |i|
    window += calories[i] - calories[i - k]
    ans -= 1 if window < lower
    ans += 1 if window > upper
  end
  ans
end
