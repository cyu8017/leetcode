# LeetCode 1498 - Number Of Subsequences That Satisfy The Given Sum Condition
# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

def num_subseq(nums, target)
  nums.sort!
  mod = 1_000_000_007
  left = 0
  right = nums.length - 1
  ans = 0
  powers = Array.new(nums.length + 1, 1)
  (1...powers.length).each { |i| powers[i] = powers[i - 1] * 2 % mod }
  while left <= right
    if nums[left] + nums[right] <= target
      ans = (ans + powers[right - left]) % mod
      left += 1
    else
      right -= 1
    end
  end
  ans
end
