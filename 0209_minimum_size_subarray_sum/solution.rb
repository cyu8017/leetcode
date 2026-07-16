# LeetCode 0209 - Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/

# @param {Integer} target
# @param {Integer[]} nums
# @return {Integer}
def min_sub_array_len(target, nums)
  left = 0
  total = 0
  best = Float::INFINITY
  nums.each_with_index do |num, right|
    total += num
    while total >= target
      best = [best, right - left + 1].min
      total -= nums[left]
      left += 1
    end
  end
  best.infinite? ? 0 : best
end