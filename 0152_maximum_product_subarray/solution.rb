# LeetCode 0152 - Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/

class Solution
  def max_product(nums)
    best = max_product = min_product = nums[0]
    nums.drop(1).each do |number|
      candidates = [number, max_product * number, min_product * number]
      max_product = candidates.max
      min_product = candidates.min
      best = [best, max_product].max
    end
    best
  end
end