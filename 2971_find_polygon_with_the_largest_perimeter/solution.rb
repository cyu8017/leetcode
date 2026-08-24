# LeetCode 2971 - Find Polygon With the Largest Perimeter
# https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/

# @param {Integer[]} nums
# @return {Integer}
def largest_perimeter(nums)
  nums.sort!
  total = nums.sum
  (nums.length - 1).downto(2) do |i|
    total -= nums[i]
    return total + nums[i] if total > nums[i]
  end
  -1
end
