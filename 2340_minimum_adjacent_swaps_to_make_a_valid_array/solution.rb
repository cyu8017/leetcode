# LeetCode 2340 - Minimum Adjacent Swaps to Make a Valid Array
# https://leetcode.com/problems/minimum-adjacent-swaps-to-make-a-valid-array/

# @param {Integer[]} nums
# @return {Integer}
def minimum_swaps(nums)
  n = nums.length
  min_i = 0
  max_i = 0
  (1...n).each do |i|
    min_i = i if nums[i] < nums[min_i]
    max_i = i if nums[i] >= nums[max_i]
  end
  ans = min_i + (n - 1 - max_i)
  ans -= 1 if min_i > max_i
  ans
end

alias solve minimum_swaps
