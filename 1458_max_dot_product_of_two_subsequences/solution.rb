# LeetCode 1458 - Max Dot Product Of Two Subsequences
# https://leetcode.com/problems/max-dot-product-of-two-subsequences/

def max_dot_product(nums1, nums2)
  n = nums2.length
  dp = Array.new(n + 1, -Float::INFINITY)
  nums1.each do |a|
    prev = dp.dup
    nums2.each_with_index do |b, idx|
      j = idx + 1
      product = a * b
      dp[j] = [dp[j - 1], prev[j], product, product + [0, prev[j - 1]].max].max
    end
  end
  dp[n].to_i
end
