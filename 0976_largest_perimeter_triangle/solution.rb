# LeetCode 0976 - Largest Perimeter Triangle
# https://leetcode.com/problems/largest-perimeter-triangle/

# @param {Integer[]} nums
# @return {Integer}
def largest_perimeter(nums)
  nums.sort! { |a, b| b <=> a }
  (0...(nums.length - 2)).each do |i|
    return nums[i] + nums[i + 1] + nums[i + 2] if nums[i] < nums[i + 1] + nums[i + 2]
  end
  0
end
