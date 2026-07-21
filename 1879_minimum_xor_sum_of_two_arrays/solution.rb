# LeetCode 1879 - Minimum XOR Sum of Two Arrays
# https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def minimum_x_o_r_sum(nums1, nums2)
  n = nums1.length
  inf = 1 << 60
  dp = Array.new(1 << n, inf)
  dp[0] = 0

  (0...(1 << n)).each do |mask|
    i = mask.digits(2).count(1)
    next if i >= n

    (0...n).each do |j|
      next if (mask & (1 << j)) != 0

      next_mask = mask | (1 << j)
      cost = dp[mask] + (nums1[i] ^ nums2[j])
      dp[next_mask] = cost if cost < dp[next_mask]
    end
  end

  dp[(1 << n) - 1]
end
