# LeetCode 3038 - Maximum Number of Operations With the Same Score I
# https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-i/

# @param {Integer[]} nums
# @return {Integer}
def max_operations(nums)
  s = nums[0] + nums[1]
  n = nums.length
  ans = 0
  i = 0
  while i + 1 < n && nums[i] + nums[i + 1] == s
    ans += 1
    i += 2
  end
  ans
end
