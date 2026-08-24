# LeetCode 2032 - Two Out of Three
# https://leetcode.com/problems/two-out-of-three/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer[]} nums3
# @return {Integer[]}
def two_out_of_three(nums1, nums2, nums3)
  s0 = nums1.to_h { |v| [v, true] }
  s1 = nums2.to_h { |v| [v, true] }
  s2 = nums3.to_h { |v| [v, true] }
  ans = []
  (1..100).each do |v|
    c = (s0[v] ? 1 : 0) + (s1[v] ? 1 : 0) + (s2[v] ? 1 : 0)
    ans << v if c >= 2
  end
  ans
end
