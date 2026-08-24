# LeetCode 2216 - Minimum Deletions to Make Array Beautiful
# https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/

# @param {Integer[]} nums
# @return {Integer}
def min_deletion(nums)
  ans = 0
  i = 0
  n = nums.length
  while i + 1 < n
    if nums[i] == nums[i + 1]
      ans += 1
      i += 1
    else
      i += 2
    end
  end
  ans += 1 if (n - ans).odd?
  ans
end
