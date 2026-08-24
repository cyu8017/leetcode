# LeetCode 3748 - Count Stable Subarrays
# https://leetcode.com/problems/count-stable-subarrays/

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer[]}
def count_stable_subarrays(nums, queries)
  n = nums.length
  seg = []
  s = [0]
  l = 0
  (0...n).each do |r|
    if r == n - 1 || nums[r] > nums[r + 1]
      seg << l
      k = r - l + 1
      s << s[-1] + k * (k + 1) / 2
      l = r + 1
    end
  end
  lower_bound = lambda do |a, x|
    lo = 0
    hi = a.length
    while lo < hi
      mid = (lo + hi) >> 1
      if a[mid] < x
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |(left, right), idx|
    i = lower_bound.call(seg, left + 1)
    j = lower_bound.call(seg, right + 1) - 1
    if i > j
      k = right - left + 1
      ans[idx] = k * (k + 1) / 2
    else
      a = seg[i] - left
      b = right - seg[j] + 1
      ans[idx] = a * (a + 1) / 2 + s[j] - s[i] + b * (b + 1) / 2
    end
  end
  ans
end
