# LeetCode 3346 - Maximum Frequency of an Element After Performing Operations I
# https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/

# @param {Integer[]} a
# @param {Integer} x
# @return {Integer}
def lower_bound(a, x)
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

# @param {Integer[]} a
# @param {Integer} x
# @return {Integer}
def upper_bound(a, x)
  lo = 0
  hi = a.length
  while lo < hi
    mid = (lo + hi) >> 1
    if a[mid] <= x
      lo = mid + 1
    else
      hi = mid
    end
  end
  lo
end

# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} num_operations
# @return {Integer}
def max_frequency(nums, k, num_operations)
  nums.sort!
  n = nums.length
  freq = {}
  nums.each { |x| freq[x] = (freq[x] || 0) + 1 }
  ans = 1
  freq.each do |t, f|
    lo = lower_bound(nums, t - k)
    hi = upper_bound(nums, t + k)
    can = hi - lo
    use = [can, f + num_operations].min
    ans = use if use > ans
  end
  l = 0
  n.times do |r|
    l += 1 while nums[r] - nums[l] > 2 * k
    window = [r - l + 1, num_operations].min
    ans = window if window > ans
  end
  ans
end
