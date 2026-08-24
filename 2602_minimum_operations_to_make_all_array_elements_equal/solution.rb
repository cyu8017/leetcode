# LeetCode 2602 - Minimum Operations to Make All Array Elements Equal
# https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/

# @param {Integer[]} nums
# @param {Integer[]} queries
# @return {Integer[]}
def min_operations(nums, queries)
  nums = nums.sort
  n = nums.length
  pref = Array.new(n + 1, 0)
  n.times { |i| pref[i + 1] = pref[i] + nums[i] }

  lower_bound = lambda do |x|
    lo = 0
    hi = n
    while lo < hi
      mid = (lo + hi) >> 1
      if nums[mid] < x
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end

  queries.map do |q|
    i = lower_bound.call(q)
    left = q * i - pref[i]
    right = pref[n] - pref[i] - q * (n - i)
    left + right
  end
end
