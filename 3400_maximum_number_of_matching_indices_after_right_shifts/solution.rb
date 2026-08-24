# LeetCode 3400 - Maximum Number of Matching Indices After Right Shifts
# https://leetcode.com/problems/maximum-number-of-matching-indices-after-right-shifts/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def maximum_matching_indices(nums1, nums2)
  n = nums1.length
  ans = 0
  (0...n).each do |shift|
    cnt = 0
    (0...n).each do |i|
      cnt += 1 if nums1[(i - shift + n) % n] == nums2[i]
    end
    ans = cnt if cnt > ans
  end
  ans
end
