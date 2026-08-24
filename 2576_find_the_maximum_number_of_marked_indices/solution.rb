# LeetCode 2576 - Find the Maximum Number of Marked Indices
# https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/

# @param {Integer[]} nums
# @return {Integer}
def max_num_of_marked_indices(nums)
  nums = nums.sort
  n = nums.length
  i = 0
  ans = 0
  ((n + 1) / 2...n).each do |j|
    if 2 * nums[i] <= nums[j]
      ans += 2
      i += 1
    end
  end
  ans
end
