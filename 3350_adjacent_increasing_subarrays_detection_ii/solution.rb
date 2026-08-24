# LeetCode 3350 - Adjacent Increasing Subarrays Detection II
# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/

# @param {Integer[]} up
# @param {Integer} n
# @param {Integer} k
# @return {Boolean}
def adjacent_inc_ok(up, n, k)
  (0..(n - 2 * k)).each do |i|
    return true if up[i] >= k && up[i + k] >= k
  end
  false
end

# @param {Integer[]} nums
# @return {Integer}
def max_increasing_subarrays(nums)
  n = nums.length
  up = Array.new(n, 0)
  up[n - 1] = 1
  (n - 2).downto(0) do |i|
    up[i] = nums[i] < nums[i + 1] ? up[i + 1] + 1 : 1
  end
  lo = 1
  hi = n / 2
  while lo < hi
    mid = (lo + hi + 1) / 2
    if adjacent_inc_ok(up, n, mid)
      lo = mid
    else
      hi = mid - 1
    end
  end
  lo
end
