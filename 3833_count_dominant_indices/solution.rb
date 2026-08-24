# LeetCode 3833 - Count Dominant Indices
# https://leetcode.com/problems/count-dominant-indices/

# @param {Integer[]} nums
# @return {Integer}
def dominant_indices(nums)
  n = nums.length
  ans = 0
  suf = nums[n - 1]
  (n - 2).downto(0) do |i|
    ans += 1 if nums[i] * (n - i - 1) > suf
    suf += nums[i]
  end
  ans
end
