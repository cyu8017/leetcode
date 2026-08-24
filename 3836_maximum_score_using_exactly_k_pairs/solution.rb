# LeetCode 3836 - Maximum Score Using Exactly K Pairs
# https://leetcode.com/problems/maximum-score-using-exactly-k-pairs/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer} k
# @return {Integer}
def max_score(nums1, nums2, k_lim)
  n = nums1.length
  m = nums2.length
  neg = -(10**18)
  f = Array.new(n + 1) { Array.new(m + 1) { Array.new(k_lim + 1, neg) } }
  f[0][0][0] = 0
  (0..n).each do |i|
    (0..m).each do |j|
      (0..k_lim).each do |k|
        f[i][j][k] = [f[i][j][k], f[i - 1][j][k]].max if i > 0
        f[i][j][k] = [f[i][j][k], f[i][j - 1][k]].max if j > 0
        if i > 0 && j > 0 && k > 0
          f[i][j][k] = [f[i][j][k], f[i - 1][j - 1][k - 1] + nums1[i - 1] * nums2[j - 1]].max
        end
      end
    end
  end
  f[n][m][k_lim]
end
