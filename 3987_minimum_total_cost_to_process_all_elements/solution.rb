# LeetCode 3987 - Minimum Total Cost to Process All Elements
# https://leetcode.com/problems/minimum-total-cost-to-process-all-elements/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def minimum_cost(nums, k)
  mod = 1_000_000_007
  cnt = 0
  cur = k
  nums.each do |x0|
    x = x0
    diff = x - cur
    if diff > 0
      m = (diff + k - 1) / k
      cur += m * k
      cnt += m
    end
    cur -= x
  end
  cnt %= mod
  (cnt + 1) * cnt / 2 % mod
end
