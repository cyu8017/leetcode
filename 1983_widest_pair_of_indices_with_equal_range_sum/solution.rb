# LeetCode 1983 - Widest Pair of Indices With Equal Range Sum
# https://leetcode.com/problems/widest-pair-of-indices-with-equal-range-sum/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def widest_pair_of_indices(nums1, nums2)
  first = { 0 => -1 }
  ans = 0
  s = 0
  nums1.zip(nums2).each_with_index do |(a, b), i|
    s += a - b
    if first.key?(s)
      ans = [ans, i - first[s]].max
    else
      first[s] = i
    end
  end
  ans
end
