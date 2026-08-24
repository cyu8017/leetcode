# LeetCode 0644 - Maximum Average Subarray II
# https://leetcode.com/problems/maximum-average-subarray-ii/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Float}
def find_max_average(nums, k)
  can_reach = lambda do |mid|
    prefix = 0.0
    k.times { |i| prefix += nums[i] - mid }
    return true if prefix >= 0

    prev = 0.0
    min_prev = 0.0
    (k...nums.length).each do |i|
      prefix += nums[i] - mid
      prev += nums[i - k] - mid
      min_prev = [min_prev, prev].min
      return true if prefix - min_prev >= 0
    end
    false
  end

  left = nums.min.to_f
  right = nums.max.to_f
  80.times do
    mid = (left + right) / 2.0
    if can_reach.call(mid)
      left = mid
    else
      right = mid
    end
  end
  left
end
