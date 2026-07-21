# LeetCode 1855 - Maximum Distance Between a Pair of Values
# https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def max_distance(nums1, nums2)
  answer = 0
  j = 0

  nums1.each_with_index do |value, i|
    while j < nums2.length && value <= nums2[j]
      j += 1
    end
    answer = [answer, j - i - 1].max
  end

  answer
end
