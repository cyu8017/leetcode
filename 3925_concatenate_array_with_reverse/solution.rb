# LeetCode 3925 - Concatenate Array With Reverse
# https://leetcode.com/problems/concatenate-array-with-reverse/

# @param {Integer[]} nums
# @return {Integer[]}
def concat_with_reverse(nums)
  n = nums.length
  ans = Array.new(2 * n, 0)
  n.times do |i|
    ans[i] = nums[i]
    ans[i + n] = nums[n - i - 1]
  end
  ans
end
