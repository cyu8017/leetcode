# LeetCode 2419 - Longest Subarray With Maximum Bitwise AND
# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

# @param {Integer[]} nums
# @return {Integer}
def longest_subarray(nums)
  mx = nums[0]
  nums.each { |x| mx = x if x > mx }
  ans = cur = 0
  nums.each do |x|
    if x == mx
      cur += 1
      ans = cur if cur > ans
    else
      cur = 0
    end
  end
  ans
end
