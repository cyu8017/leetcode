# LeetCode 1918 - Kth Smallest Subarray Sum
# https://leetcode.com/problems/kth-smallest-subarray-sum/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def kth_smallest_subarray_sum(nums, k)
  count = lambda do |limit|
    total = left = ans = 0
    nums.each_with_index do |value, right|
      total += value
      while total > limit
        total -= nums[left]
        left += 1
      end
      ans += right - left + 1
    end
    ans
  end
  lo = nums.min
  hi = nums.sum
  while lo < hi
    mid = (lo + hi) / 2
    if count.call(mid) >= k
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
