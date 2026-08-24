# LeetCode 2348 - Number of Zero-Filled Subarrays
# https://leetcode.com/problems/number-of-zero-filled-subarrays/

# @param {Integer[]} nums
# @return {Integer}
def zero_filled_subarray(nums)
  ans = 0
  streak = 0
  nums.each do |x|
    if x == 0
      streak += 1
      ans += streak
    else
      streak = 0
    end
  end
  ans
end
