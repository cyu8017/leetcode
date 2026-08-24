# LeetCode 2016 - Maximum Difference Between Increasing Elements
# https://leetcode.com/problems/maximum-difference-between-increasing-elements/

# @param {Integer[]} nums
# @return {Integer}
def maximum_difference(nums)
  ans = -1
  mn = nums[0]
  (1...nums.length).each do |i|
    if nums[i] > mn
      ans = [ans, nums[i] - mn].max
    else
      mn = nums[i]
    end
  end
  ans
end
