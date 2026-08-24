# LeetCode 3972 - Valid Subarrays With Matching Sum Digits II
# https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-ii/

# @param {Integer[]} nums
# @param {Integer} x
# @return {Integer}
def count_valid_subarrays(nums, x)
  lower_bound = lambda do |a, val|
    lo = 0
    hi = a.length
    while lo < hi
      mid = (lo + hi) / 2
      if a[mid] < val
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end
  upper_bound = lambda do |a, val|
    lo = 0
    hi = a.length
    while lo < hi
      mid = (lo + hi) / 2
      if a[mid] <= val
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end
  by_remainder = Array.new(10) { [] }
  by_remainder[0] << 0
  prefix = 0
  answer = 0
  nums.each do |value|
    prefix += value
    required = ((prefix - x) % 10 + 10) % 10
    values = by_remainder[required]
    power = 1
    while x * power <= prefix
      low = x * power
      high = (x + 1) * power - 1
      min_prefix = prefix - high
      max_prefix = prefix - low
      left = lower_bound.call(values, min_prefix)
      right = upper_bound.call(values, max_prefix)
      answer += right - left
      break if power > prefix / 10
      power *= 10
    end
    by_remainder[prefix % 10] << prefix
  end
  answer
end
