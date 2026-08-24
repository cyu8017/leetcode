# LeetCode 2859 - Sum of Values at Indices With K Set Bits
# https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def sum_indices_with_k_set_bits(nums, k)
  ans = 0
  nums.each_with_index do |val, i|
    x = i
    bits = 0
    while x > 0
      bits += x & 1
      x >>= 1
    end
    ans += val if bits == k
  end
  ans
end
