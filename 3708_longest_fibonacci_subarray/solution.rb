# LeetCode 3708 - Longest Fibonacci Subarray
# https://leetcode.com/problems/longest-fibonacci-subarray/

# @param {Integer[]} nums
# @return {Integer}
def longest_subarray(nums)
  f = 2
  ans = f
  (2...nums.length).each do |i|
    if nums[i] == nums[i - 1] + nums[i - 2]
      f += 1
      ans = f if f > ans
    else
      f = 2
    end
  end
  ans
end
