# LeetCode 0719 - Find K-th Smallest Pair Distance
# https://leetcode.com/problems/find-k-th-smallest-pair-distance/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def smallest_distance_pair(nums, k)
  nums = nums.sort
  count_pairs = lambda do |distance|
    count = 0
    left = 0
    nums.each_with_index do |value, right|
      left += 1 while value - nums[left] > distance
      count += right - left
    end
    count
  end

  lo = 0
  hi = nums[-1] - nums[0]
  while lo < hi
    mid = (lo + hi) / 2
    if count_pairs.call(mid) >= k
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
