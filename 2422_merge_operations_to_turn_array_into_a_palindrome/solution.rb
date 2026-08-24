# LeetCode 2422 - Merge Operations to Turn Array Into a Palindrome
# https://leetcode.com/problems/merge-operations-to-turn-array-into-a-palindrome/

# @param {Integer[]} nums
# @return {Integer}
def minimum_operations(nums)
  l = 0
  r = nums.length - 1
  left = nums[l]
  right = nums[r]
  ans = 0
  while l < r
    if left == right
      l += 1
      r -= 1
      if l < r
        left = nums[l]
        right = nums[r]
      end
    elsif left < right
      l += 1
      left += nums[l]
      ans += 1
    else
      r -= 1
      right += nums[r]
      ans += 1
    end
  end
  ans
end
