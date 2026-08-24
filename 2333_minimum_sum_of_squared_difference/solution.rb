# LeetCode 2333 - Minimum Sum of Squared Difference
# https://leetcode.com/problems/minimum-sum-of-squared-difference/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer} k1
# @param {Integer} k2
# @return {Integer}
def min_sum_square_diff(nums1, nums2, k1, k2)
  n = nums1.length
  diff = Array.new(n, 0)
  max_d = 0
  (0...n).each do |i|
    d = (nums1[i] - nums2[i]).abs
    diff[i] = d
    max_d = d if d > max_d
  end
  k = k1 + k2
  freq = Array.new(max_d + 1, 0)
  diff.each { |d| freq[d] += 1 }
  max_d.downto(1) do |d|
    break if k <= 0
    next if freq[d] == 0
    take = freq[d]
    take = k if take > k
    freq[d] -= take
    freq[d - 1] += take
    k -= take
  end
  ans = 0
  (0..max_d).each { |d| ans += d * d * freq[d] }
  ans
end
