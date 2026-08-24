# LeetCode 3284 - Sum of Consecutive Subarrays
# https://leetcode.com/problems/sum-of-consecutive-subarrays/

# @param {Integer[]} nums
# @return {Integer}
def range_sum(nums)
  mod = 1_000_000_007
  n = nums.length
  ans = 0
  i = 0
  while i < n
    j = i
    j += 1 while j + 1 < n && (nums[j + 1] == nums[j] + 1 || nums[j + 1] == nums[j] - 1)
    (i..j).each do |l|
      s = 0
      (l..j).each do |r|
        s += nums[r]
        ans = (ans + s) % mod
      end
    end
    i = j + 1
  end
  ans
end
