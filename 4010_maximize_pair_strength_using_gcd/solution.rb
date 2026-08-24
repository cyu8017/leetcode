# LeetCode 4010 - Maximize Pair Strength Using GCD
# https://leetcode.com/problems/maximize-pair-strength-using-gcd/

# @param {Integer[]} nums
# @return {Integer}
def max_pair_strength(nums)
  gcd = lambda do |a, b|
    while b != 0
      a, b = b, a % b
    end
    a
  end
  n = nums.length
  ans = 0
  n.times do |i|
    ((i + 1)...n).each do |j|
      g = gcd.call(nums[i], nums[j])
      x = nums[i] * nums[j] / (g * g)
      ans = x if x > ans
    end
  end
  ans
end
