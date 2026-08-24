# LeetCode 3919 - Minimum Cost to Move Between Indices
# https://leetcode.com/problems/minimum-cost-to-move-between-indices/

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer[]}
def min_cost(nums, queries)
  n = nums.length
  s1 = Array.new(n, 0)
  s2 = Array.new(n, 0)
  (1...n).each do |i|
    c1 = 1
    c1 = nums[i] - nums[i - 1] if i > 1 && nums[i - 1] - nums[i - 2] <= nums[i] - nums[i - 1]
    c2 = 1
    c2 = nums[i] - nums[i - 1] if i < n - 1 && nums[i] - nums[i - 1] > nums[i + 1] - nums[i]
    s1[i] = s1[i - 1] + c1
    s2[i] = s2[i - 1] + c2
  end
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, i|
    l, r = q[0], q[1]
    ans[i] = l < r ? s1[r] - s1[l] : s2[l] - s2[r]
  end
  ans
end
