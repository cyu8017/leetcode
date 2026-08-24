# LeetCode 3911 - K-th Smallest Remaining Even Integer in Subarray Queries
# https://leetcode.com/problems/k-th-smallest-remaining-even-integer-in-subarray-queries/

def upper_bound3911(a, x)
  lo = 0
  hi = a.length
  while lo < hi
    mid = (lo + hi) / 2
    if a[mid] <= x
      lo = mid + 1
    else
      hi = mid
    end
  end
  lo
end

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer[]}
def kth_smallest_even(nums, queries)
  n = nums.length
  even_prefix = Array.new(n + 1, 0)
  n.times { |i| even_prefix[i + 1] = even_prefix[i] + (nums[i].even? ? 1 : 0) }
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, qi|
    l, r, k = q[0], q[1], q[2]
    lo = 1
    hi = k + (r - l + 1)
    while lo < hi
      mid = (lo + hi) / 2
      pos = upper_bound3911(nums, 2 * mid)
      pos = r + 1 if pos > r + 1
      removed = pos > l ? even_prefix[pos] - even_prefix[l] : 0
      if mid - removed >= k
        hi = mid
      else
        lo = mid + 1
      end
    end
    ans[qi] = 2 * lo
  end
  ans
end
