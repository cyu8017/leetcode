# LeetCode 0053 - Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/

# @param {Integer[]} nums
# @return {Integer}
def max_sub_array(nums)
  best = nums[0]
  current = nums[0]

  (1...nums.length).each do |i|
    current = [nums[i], current + nums[i]].max
    best = [best, current].max
  end

  best
end
