# LeetCode 2607 - Make K-Subarray Sums Equal
# https://leetcode.com/problems/make-k-subarray-sums-equal/

# @param {Integer[]} arr
# @param {Integer} k
# @return {Integer}
def make_sub_k_sum_equal(arr, k)
  n = arr.length
  g = n.gcd(k)
  ans = 0
  g.times do |r|
    group = (r...n).step(g).map { |i| arr[i] }
    group.sort!
    med = group[group.length / 2]
    group.each { |x| ans += (x - med).abs }
  end
  ans
end
