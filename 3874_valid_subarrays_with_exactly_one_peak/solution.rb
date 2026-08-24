# LeetCode 3874 - Valid Subarrays With Exactly One Peak
# https://leetcode.com/problems/valid-subarrays-with-exactly-one-peak/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def valid_subarrays(nums, k)
  n = nums.length
  peaks = []
  (1...(n - 1)).each do |i|
    peaks << i if nums[i] > nums[i - 1] && nums[i] > nums[i + 1]
  end
  ans = 0
  peaks.each_with_index do |p, j|
    left_min = [p - k, 0].max
    left_min = [left_min, peaks[j - 1] + 1].max if j > 0
    right_max = [p + k, n - 1].min
    right_max = [right_max, peaks[j + 1] - 1].min if j < peaks.length - 1
    ans += (p - left_min + 1) * (right_max - p + 1)
  end
  ans
end
