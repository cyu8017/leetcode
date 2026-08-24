# LeetCode 3795 - Minimum Subarray Length with Distinct Sum at Least K
# https://leetcode.com/problems/minimum-subarray-length-with-distinct-sum-at-least-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_length(nums, k)
  n = nums.length
  ans = n + 1
  l = 0
  cnt = Hash.new(0)
  s = 0
  (0...n).each do |r|
    c = cnt[nums[r]] + 1
    cnt[nums[r]] = c
    s += nums[r] if c == 1
    while s >= k
      ans = r - l + 1 if r - l + 1 < ans
      left = nums[l]
      nc = cnt[left] - 1
      if nc == 0
        cnt.delete(left)
        s -= left
      else
        cnt[left] = nc
      end
      l += 1
    end
  end
  ans > n ? -1 : ans
end
