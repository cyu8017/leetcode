# LeetCode 3768 - Minimum Inversion Count in Subarrays of Fixed Length
# https://leetcode.com/problems/minimum-inversion-count-in-subarrays-of-fixed-length/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_inversion_count(nums, k)
  vals = nums.sort
  n = 0
  (0...vals.length).each do |i|
    if n == 0 || vals[i] != vals[n - 1]
      vals[n] = vals[i]
      n += 1
    end
  end
  vals = vals[0, n]
  bit = Array.new(vals.length + 1, 0)
  add = lambda do |i, delta|
    while i < bit.length
      bit[i] += delta
      i += i & -i
    end
  end
  sum_fn = lambda do |i|
    res = 0
    while i > 0
      res += bit[i]
      i -= i & -i
    end
    res
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
  rank = Array.new(nums.length, 0)
  inv = 0
  (0...nums.length).each do |i|
    rank[i] = lower_bound.call(vals, nums[i]) + 1
    if i < k
      inv += i - sum_fn.call(rank[i])
      add.call(rank[i], 1)
    end
  end
  best = inv
  (k...nums.length).each do |r|
    left = rank[r - k]
    inv -= sum_fn.call(left - 1)
    add.call(left, -1)
    inv += k - 1 - sum_fn.call(rank[r])
    add.call(rank[r], 1)
    best = inv if inv < best
  end
  best
end
