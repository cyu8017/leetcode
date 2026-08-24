# LeetCode 2918 - Minimum Equal Sum of Two Arrays After Replacing Zeros
# https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def min_sum(nums1, nums2)
  s1 = s2 = z1 = z2 = 0
  nums1.each do |v|
    if v == 0
      z1 += 1
      s1 += 1
    else
      s1 += v
    end
  end
  nums2.each do |v|
    if v == 0
      z2 += 1
      s2 += 1
    else
      s2 += v
    end
  end
  return -1 if z1 == 0 && s1 < s2
  return -1 if z2 == 0 && s2 < s1

  s1 > s2 ? s1 : s2
end
