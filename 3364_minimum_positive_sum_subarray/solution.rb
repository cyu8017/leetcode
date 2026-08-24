# LeetCode 3364 - Minimum Positive Sum Subarray
# https://leetcode.com/problems/minimum-positive-sum-subarray/

# @param {Integer[]} nums
# @param {Integer} l
# @param {Integer} r
# @return {Integer}
def minimum_sum_subarray(nums, l, r)
  n = nums.length
  pref = Array.new(n + 1, 0)
  n.times { |i| pref[i + 1] = pref[i] + nums[i] }
  ans = 2_147_483_647
  found = false
  n.times do |i|
    length = l
    while length <= r && i + length <= n
      s = pref[i + length] - pref[i]
      if s > 0 && s < ans
        ans = s
        found = true
      end
      length += 1
    end
  end
  found ? ans : -1
end
