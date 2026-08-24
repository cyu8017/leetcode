# LeetCode 3073 - Maximum Increasing Triplet Value
# https://leetcode.com/problems/maximum-increasing-triplet-value/

# @param {Integer[]} nums
# @return {Integer}
def maximum_triplet_value(nums)
  n = nums.length
  right = Array.new(n, 0)
  right[n - 1] = nums[n - 1]
  (n - 2).downto(0) { |i| right[i] = [nums[i], right[i + 1]].max }
  ts = []

  add = lambda do |x|
    lo = 0
    hi = ts.length
    while lo < hi
      mid = (lo + hi) >> 1
      if ts[mid] < x
        lo = mid + 1
      else
        hi = mid
      end
    end
    ts.insert(lo, x) if lo == ts.length || ts[lo] != x
  end

  lower = lambda do |x|
    lo = 0
    hi = ts.length
    while lo < hi
      mid = (lo + hi) >> 1
      if ts[mid] < x
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo > 0 ? ts[lo - 1] : nil
  end

  add.call(nums[0])
  ans = 0
  (1...n - 1).each do |j|
    if right[j + 1] > nums[j]
      it = lower.call(nums[j])
      ans = [ans, it - nums[j] + right[j + 1]].max if it
    end
    add.call(nums[j])
  end
  ans
end
