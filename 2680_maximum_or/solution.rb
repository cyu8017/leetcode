# LeetCode 2680 - Maximum OR
# https://leetcode.com/problems/maximum-or/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximum_or(nums, k)
  n = nums.length
  pref = Array.new(n + 1, 0)
  suf = Array.new(n + 1, 0)
  n.times { |i| pref[i + 1] = pref[i] | nums[i] }
  (n - 1).downto(0) { |i| suf[i] = suf[i + 1] | nums[i] }
  ans = 0
  n.times do |i|
    cur = pref[i] | (nums[i] * (2**k)) | suf[i + 1]
    ans = cur if cur > ans
  end
  ans
end
