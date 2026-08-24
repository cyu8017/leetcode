# LeetCode 3427 - Sum of Variable Length Subarrays
# https://leetcode.com/problems/sum-of-variable-length-subarrays/

# @param {Integer[]} nums
# @return {Integer}
def subarray_sum(nums)
  n = nums.length
  pref = Array.new(n + 1, 0)
  (0...n).each { |i| pref[i + 1] = pref[i] + nums[i] }
  ans = 0
  (0...n).each do |i|
    start = i - nums[i]
    start = 0 if start < 0
    ans += pref[i + 1] - pref[start]
  end
  ans
end
