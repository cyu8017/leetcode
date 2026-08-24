# LeetCode 2393 - Count Strictly Increasing Subarrays
# https://leetcode.com/problems/count-strictly-increasing-subarrays/

# @param {Integer[]} nums
# @return {Integer}
def count_subarrays(nums)
  ans = 0
  length = 0
  nums.each_index do |i|
    if i > 0 && nums[i] > nums[i - 1]
      length += 1
    else
      length = 1
    end
    ans += length
  end
  ans
end

alias solve count_subarrays
