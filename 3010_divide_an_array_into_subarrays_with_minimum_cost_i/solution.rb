# LeetCode 3010 - Divide an Array Into Subarrays With Minimum Cost I
# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/

# @param {Integer[]} nums
# @return {Integer}
def minimum_cost(nums)
  a = nums[0]
  b = 100
  c = 100
  (1...nums.length).each do |i|
    x = nums[i]
    if x < b
      c = b
      b = x
    elsif x < c
      c = x
    end
  end
  a + b + c
end
