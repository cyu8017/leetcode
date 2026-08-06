# LeetCode 1283 - Find the Smallest Divisor Given a Threshold
# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

# @param {Integer[]} nums
# @param {Integer} threshold
# @return {Integer}
def smallest_divisor(nums, threshold)
  lo = 1
  hi = nums.max
  while lo < hi
    mid = (lo + hi) / 2
    if nums.sum { |x| (x + mid - 1) / mid } <= threshold
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
