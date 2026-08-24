# LeetCode 3420 - Count Non-Decreasing Subarrays After K Operations
# https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_non_decreasing_subarrays(nums, k)
  n = nums.length
  ans = 0
  (0...n).each do |i|
    cost = 0
    max_v = nums[i]
    (i...n).each do |j|
      if nums[j] >= max_v
        max_v = nums[j]
      else
        cost += max_v - nums[j]
      end
      break if cost > k

      ans += 1
    end
  end
  ans
end
