# LeetCode 3139 - Minimum Cost to Equalize Array
# https://leetcode.com/problems/minimum-cost-to-equalize-array/

# @param {Integer[]} nums
# @param {Integer} cost1
# @param {Integer} cost2
# @return {Integer}
def min_cost_to_equalize_array(nums, cost1, cost2)
  mod = 1_000_000_007
  n = nums.length
  min_num = nums.min
  max_num = nums.max
  total = nums.sum
  if cost1 * 2 <= cost2 || n < 3
    total_gap = max_num * n - total
    return (cost1 * total_gap) % mod
  end
  ans = 10**18
  (max_num...2 * max_num).each do |target|
    max_gap = target - min_num
    total_gap = target * n - total
    pairs = total_gap / 2
    alt = total_gap - max_gap
    pairs = alt if alt < pairs
    cost = cost1 * (total_gap - 2 * pairs) + cost2 * pairs
    ans = [ans, cost].min
  end
  ans % mod
end
