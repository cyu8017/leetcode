# LeetCode 3026 - Maximum Good Subarray Sum
# https://leetcode.com/problems/maximum-good-subarray-sum/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximum_subarray_sum(nums, k)
  p = {}
  p[nums[0]] = 0
  s = 0
  n = nums.length
  ans = -1 << 60
  n.times do |i|
    s += nums[i]
    ans = [ans, s - p[nums[i] - k]].max if p.key?(nums[i] - k)
    ans = [ans, s - p[nums[i] + k]].max if p.key?(nums[i] + k)
    break if i + 1 == n

    old = p[nums[i + 1]]
    p[nums[i + 1]] = s if old.nil? || s < old
  end
  ans == (-1 << 60) ? 0 : ans
end
