# LeetCode 2708 - Maximum Strength of a Group
# https://leetcode.com/problems/maximum-strength-of-a-group/

# @param {Integer[]} nums
# @return {Integer}
def max_strength(nums)
  nums = nums.sort
  n = nums.length
  return nums[0] if n == 1

  prod = 1
  used = false
  i = 0
  while i + 1 < n && nums[i] < 0 && nums[i + 1] < 0
    prod *= nums[i] * nums[i + 1]
    used = true
    i += 2
  end
  neg_left = i < n && nums[i] < 0
  while i < n
    if nums[i] > 0
      prod *= nums[i]
      used = true
    end
    i += 1
  end
  unless used
    if neg_left
      nums.each { |x| return 0 if x == 0 }
      return nums[n - 1]
    end
    return 0
  end
  prod
end
