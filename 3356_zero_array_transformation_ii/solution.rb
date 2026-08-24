# LeetCode 3356 - Zero Array Transformation II
# https://leetcode.com/problems/zero-array-transformation-ii/

# @param {Integer} k
# @param {Integer[]} nums
# @param {Integer[][]} queries
# @param {Integer} n
# @return {Boolean}
def zero_array_ok(k, nums, queries, n)
  diff = Array.new(n + 1, 0)
  k.times do |i|
    q = queries[i]
    diff[q[0]] += q[2]
    diff[q[1] + 1] -= q[2]
  end
  cur = 0
  n.times do |i|
    cur += diff[i]
    return false if cur < nums[i]
  end
  true
end

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer}
def min_zero_array(nums, queries)
  n = nums.length
  return 0 if zero_array_ok(0, nums, queries, n)

  lo = 1
  hi = queries.length + 1
  while lo < hi
    mid = (lo + hi) >> 1
    if mid <= queries.length && zero_array_ok(mid, nums, queries, n)
      hi = mid
    else
      lo = mid + 1
    end
  end
  return -1 if lo > queries.length

  lo
end
