# LeetCode 2570 - Merge Two 2D Arrays by Summing Values
# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/

# @param {Integer[][]} nums1
# @param {Integer[][]} nums2
# @return {Integer[][]}
def merge_arrays(nums1, nums2)
  ans = []
  i = j = 0
  while i < nums1.length && j < nums2.length
    if nums1[i][0] == nums2[j][0]
      ans << [nums1[i][0], nums1[i][1] + nums2[j][1]]
      i += 1
      j += 1
    elsif nums1[i][0] < nums2[j][0]
      ans << [nums1[i][0], nums1[i][1]]
      i += 1
    else
      ans << [nums2[j][0], nums2[j][1]]
      j += 1
    end
  end
  while i < nums1.length
    ans << [nums1[i][0], nums1[i][1]]
    i += 1
  end
  while j < nums2.length
    ans << [nums2[j][0], nums2[j][1]]
    j += 1
  end
  ans
end
