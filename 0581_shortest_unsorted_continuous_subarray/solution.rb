# LeetCode 0581 - Shortest Unsorted Continuous Subarray
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

# @param {Integer[]} nums
# @return {Integer}
def find_unsorted_subarray(nums)
  n = nums.length
  left = -1
  right = -2
  max_seen = nums[0]
  min_seen = nums[-1]

  n.times do |i|
    max_seen = [max_seen, nums[i]].max
    right = i if nums[i] < max_seen
    min_seen = [min_seen, nums[n - 1 - i]].min
    left = n - 1 - i if nums[n - 1 - i] > min_seen
  end

  right - left + 1
end
