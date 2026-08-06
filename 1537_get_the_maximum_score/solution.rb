# LeetCode 1537 - Get the Maximum Score
# https://leetcode.com/problems/get-the-maximum-score/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def max_sum(nums1, nums2)
  i = j = first = second = 0
  while i < nums1.length || j < nums2.length
    if j == nums2.length || (i < nums1.length && nums1[i] < nums2[j])
      first += nums1[i]
      i += 1
    elsif i == nums1.length || nums2[j] < nums1[i]
      second += nums2[j]
      j += 1
    else
      first = second = [first, second].max + nums1[i]
      i += 1
      j += 1
    end
  end
  [first, second].max % 1_000_000_007
end
