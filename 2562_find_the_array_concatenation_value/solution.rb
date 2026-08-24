# LeetCode 2562 - Find the Array Concatenation Value
# https://leetcode.com/problems/find-the-array-concatenation-value/

# @param {Integer[]} nums
# @return {Integer}
def find_the_array_conc_val(nums)
  ans = 0
  l = 0
  r = nums.length - 1
  while l <= r
    if l == r
      ans += nums[l]
      break
    end
    left = nums[l]
    right = nums[r]
    p = 1
    t = right
    while t > 0
      p *= 10
      t /= 10
    end
    ans += left * p + right
    l += 1
    r -= 1
  end
  ans
end
