# LeetCode 1800 - Maximum Ascending Subarray Sum
# https://leetcode.com/problems/maximum-ascending-subarray-sum/

# @param {Integer[]} nums
# @return {Integer}
def max_ascending_sum(nums)
  best = nums[0]
  cur = nums[0]
  (1...nums.length).each do |i|
    cur = nums[i] > nums[i - 1] ? cur + nums[i] : nums[i]
    best = cur if cur > best
  end
  best
end
