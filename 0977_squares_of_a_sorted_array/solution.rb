# LeetCode 0977 - Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/

# @param {Integer[]} nums
# @return {Integer[]}
def sorted_squares(nums)
  n = nums.length
  ans = Array.new(n, 0)
  i = 0
  j = n - 1
  (n - 1).downto(0) do |k|
    if nums[i].abs > nums[j].abs
      ans[k] = nums[i] * nums[i]
      i += 1
    else
      ans[k] = nums[j] * nums[j]
      j -= 1
    end
  end
  ans
end
