# LeetCode 3300 - Minimum Element After Replacement With Digit Sum
# https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/

# @param {Integer[]} nums
# @return {Integer}
def min_element(nums)
  ans = 1_000_000_000
  nums.each do |num|
    x = num
    s = 0
    while x > 0
      s += x % 10
      x /= 10
    end
    ans = s if s < ans
  end
  ans
end
