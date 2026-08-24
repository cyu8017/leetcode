# LeetCode 2817 - Minimum Absolute Difference Between Elements With Constraint
# https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/

# @param {Integer[]} nums
# @param {Integer} x
# @return {Integer}
def min_absolute_difference(nums, x)
  if x == 0
    ans0 = 10**18
    (1...nums.length).each { |i| ans0 = [ans0, (nums[i] - nums[i - 1]).abs].min }
    return ans0
  end
  ans = 10**18
  arr = []
  insert = lambda do |v|
    lo = 0
    hi = arr.length
    while lo < hi
      mid = (lo + hi) >> 1
      if arr[mid] < v
        lo = mid + 1
      else
        hi = mid
      end
    end
    arr.insert(lo, v)
  end
  lower_bound = lambda do |v|
    lo = 0
    hi = arr.length
    while lo < hi
      mid = (lo + hi) >> 1
      if arr[mid] < v
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end
  (x...nums.length).each do |i|
    insert.call(nums[i - x])
    cur = nums[i]
    idx = lower_bound.call(cur)
    ans = [ans, arr[idx] - cur].min if idx < arr.length
    ans = [ans, cur - arr[idx - 1]].min if idx > 0
  end
  ans
end
