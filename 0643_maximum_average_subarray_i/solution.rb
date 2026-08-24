# LeetCode 0643 - Maximum Average Subarray I
# https://leetcode.com/problems/maximum-average-subarray-i/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Float}
def find_max_average(nums, k)
  window = nums[0, k].sum
  best = window
  (k...nums.length).each do |i|
    window += nums[i] - nums[i - k]
    best = [best, window].max
  end
  best.to_f / k
end
