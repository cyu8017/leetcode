# LeetCode 1712 - Ways to Split Array Into Three Subarrays
# https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/

# @param {Integer[]} nums
# @return {Integer}
def ways_to_split(nums)
  mod = 10**9 + 7
  n = nums.length
  prefix = []
  total = 0
  nums.each do |value|
    total += value
    prefix << total
  end

  lower_bound = lambda do |target, lo, hi|
    while lo < hi
      mid = (lo + hi) / 2
      if prefix[mid] < target
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end

  upper_bound = lambda do |target, lo, hi|
    while lo < hi
      mid = (lo + hi) / 2
      if prefix[mid] <= target
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end

  ans = 0
  (0...(n - 2)).each do |i|
    left = prefix[i]
    lo = lower_bound.call(2 * left, i + 1, n - 1)
    hi = upper_bound.call((total + left) / 2, lo, n - 1)
    ans = (ans + hi - lo) % mod
  end
  ans
end
