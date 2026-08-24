# LeetCode 2270 - Number of Ways to Split Array
# https://leetcode.com/problems/number-of-ways-to-split-array/

# @param {Integer[]} nums
# @return {Integer}
def ways_to_split_array(nums)
  total = nums.sum
  left = ans = 0
  (0...(nums.length - 1)).each do |i|
    left += nums[i]
    ans += 1 if left >= total - left
  end
  ans
end
