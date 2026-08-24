# LeetCode 2448 - Minimum Cost to Make Array Equal
# https://leetcode.com/problems/minimum-cost-to-make-array-equal/

# @param {Integer[]} nums
# @param {Integer[]} cost
# @return {Integer}
def min_cost(nums, cost)
  n = nums.length
  idx = (0...n).to_a
  idx.sort_by! { |i| nums[i] }
  total_cost = cost.sum
  pref = 0
  median = 0
  idx.each do |i|
    pref += cost[i]
    if pref * 2 >= total_cost
      median = nums[i]
      break
    end
  end
  ans = 0
  (0...n).each do |i|
    diff = nums[i] - median
    diff = -diff if diff < 0
    ans += diff * cost[i]
  end
  ans
end
