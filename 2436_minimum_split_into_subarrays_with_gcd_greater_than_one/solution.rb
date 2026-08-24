# LeetCode 2436 - Minimum Split Into Subarrays With GCD Greater Than One
# https://leetcode.com/problems/minimum-split-into-subarrays-with-gcd-greater-than-one/

# @param {Integer[]} nums
# @return {Integer}
def minimum_splits(nums)
  gcd = lambda do |a, b|
    while b != 0
      a, b = b, a % b
    end
    a
  end

  ans = 1
  g = nums[0]
  (1...nums.length).each do |i|
    ng = gcd.call(g, nums[i])
    if ng == 1
      ans += 1
      g = nums[i]
    else
      g = ng
    end
  end
  ans
end
