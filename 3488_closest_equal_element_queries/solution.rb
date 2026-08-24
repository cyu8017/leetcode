# LeetCode 3488 - Closest Equal Element Queries
# https://leetcode.com/problems/closest-equal-element-queries/

# @param {Integer[]} nums
# @param {Integer[]} queries
# @return {Integer[]}
def solve_queries(nums, queries)
  n = nums.length
  pos = {}
  nums.each_with_index do |x, i|
    pos[x] ||= []
    pos[x] << i
  end
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |idx, qi|
    x = nums[idx]
    arr = pos[x]
    if arr.length == 1
      ans[qi] = -1
      next
    end
    best = n
    arr.each do |p|
      next if p == idx

      d = (p - idx).abs
      d = [d, n - d].min
      best = d if d < best
    end
    ans[qi] = best
  end
  ans
end
