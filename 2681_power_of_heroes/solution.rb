# LeetCode 2681 - Power of Heroes
# https://leetcode.com/problems/power-of-heroes/

# @param {Integer[]} nums
# @return {Integer}
def sum_of_power(nums)
  mod = 1_000_000_007
  nums = nums.sort
  ans = 0
  s = 0
  nums.each do |x|
    ans = (ans + ((s + x) % mod) * x % mod * x) % mod
    s = (s * 2 + x) % mod
  end
  ans
end
