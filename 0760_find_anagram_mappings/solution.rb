# LeetCode 0760 - Find Anagram Mappings
# https://leetcode.com/problems/find-anagram-mappings/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer[]}
def anagram_mappings(nums1, nums2)
  positions = Hash.new { |h, k| h[k] = [] }
  nums2.each_with_index { |value, index| positions[value] << index }
  nums1.map { |value| positions[value].shift }
end
