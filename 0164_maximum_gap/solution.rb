# LeetCode 0164 - Maximum Gap
# https://leetcode.com/problems/maximum-gap/

class Solution
  def maximum_gap(nums)
    return 0 if nums.length < 2 || nums.min == nums.max

    low = nums.min
    high = nums.max
    bucket_size = [(high - low) / (nums.length - 1), 1].max
    bucket_count = (high - low) / bucket_size + 1
    mins = Array.new(bucket_count, Float::INFINITY)
    maxs = Array.new(bucket_count, -Float::INFINITY)
    used = Array.new(bucket_count, false)
    nums.each do |number|
      index = (number - low) / bucket_size
      used[index] = true
      mins[index] = [mins[index], number].min
      maxs[index] = [maxs[index], number].max
    end
    best = 0
    previous_max = low
    bucket_count.times do |index|
      next unless used[index]

      best = [best, mins[index] - previous_max].max
      previous_max = maxs[index]
    end
    best
  end
end