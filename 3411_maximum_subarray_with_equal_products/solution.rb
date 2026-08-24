# LeetCode 3411 - Maximum Subarray With Equal Products
# https://leetcode.com/problems/maximum-subarray-with-equal-products/

# @param {Integer[]} nums
# @return {Integer}
def max_length(nums)
  n = nums.length
  ans = 1
  (0...n).each do |i|
    prod = 1
    g = 0
    l = 1
    (i...n).each do |j|
      break if prod > 1_000_000_000 / nums[j]

      prod *= nums[j]
      if g == 0
        g = nums[j]
        l = nums[j]
      else
        g = gcd_3411(g, nums[j])
        l = l / gcd_3411(l, nums[j]) * nums[j]
      end
      ans = j - i + 1 if prod == l * g && j - i + 1 > ans
    end
  end
  ans
end

def gcd_3411(a, b)
  while b != 0
    a, b = b, a % b
  end
  a
end
