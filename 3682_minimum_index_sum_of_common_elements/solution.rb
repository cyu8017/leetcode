# LeetCode 3682 - Minimum Index Sum of Common Elements
# https://leetcode.com/problems/minimum-index-sum-of-common-elements/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def minimum_sum(nums1, nums2)
  inf = 1 << 30
  d = {}
  nums2.each_with_index { |x, i| d[x] = i unless d.key?(x) }
  ans = inf
  nums1.each_with_index do |x, i|
    ans = [ans, i + d[x]].min if d.key?(x)
  end
  ans == inf ? -1 : ans
end
