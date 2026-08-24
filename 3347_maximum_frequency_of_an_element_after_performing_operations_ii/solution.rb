# LeetCode 3347 - Maximum Frequency of an Element After Performing Operations II
# https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/

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
  freq = {}
  nums.each { |x| freq[x] = (freq[x] || 0) + 1 }
  ans = 1
  candidates = []
  seen = {}
  nums.each do |x|
    [x - k, x, x + k].each do |t|
      unless seen[t]
        seen[t] = true
        candidates << t
      end
    end
  end
  candidates.each do |t|
    lo = lower_bound(nums, t - k)
    hi = upper_bound(nums, t + k)
    can = hi - lo
    f = freq[t] || 0
    use = [can, f + num_operations].min
    ans = use if use > ans
  end
  ans
end
