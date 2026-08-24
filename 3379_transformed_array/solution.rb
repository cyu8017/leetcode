# LeetCode 3379 - Transformed Array
# https://leetcode.com/problems/transformed-array/

# @param {Integer[]} nums
# @return {Integer[]}
def construct_transformed_array(nums)
  n = nums.length
  ans = Array.new(n, 0)
  n.times do |i|
    j = ((i + nums[i]) % n + n) % n
    ans[i] = nums[j]
  end
  ans
end
