# LeetCode 2398 - Maximum Number of Robots Within Budget
# https://leetcode.com/problems/maximum-number-of-robots-within-budget/

# @param {Integer[]} charge_times
# @param {Integer[]} running_costs
# @param {Integer} budget
# @return {Integer}
def maximum_robots(charge_times, running_costs, budget)
  n = charge_times.length
  left = 0
  s = 0
  dq = []
  ans = 0
  (0...n).each do |right|
    dq.pop while !dq.empty? && charge_times[dq[-1]] <= charge_times[right]
    dq << right
    s += running_costs[right]
    while left <= right && charge_times[dq[0]] + (right - left + 1) * s > budget
      dq.shift if dq[0] == left
      s -= running_costs[left]
      left += 1
    end
    cand = right - left + 1
    ans = cand if cand > ans
  end
  ans
end
