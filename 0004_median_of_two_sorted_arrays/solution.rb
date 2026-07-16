# LeetCode 0004 - Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Float}
def find_median_sorted_arrays(nums1, nums2)
  nums1, nums2 = nums2, nums1 if nums1.length > nums2.length

  m = nums1.length
  n = nums2.length
  total_left = (m + n + 1) / 2
  lo = 0
  hi = m

  while lo <= hi
    i = (lo + hi) / 2
    j = total_left - i

    nums1_left_max = i.zero? ? -Float::INFINITY : nums1[i - 1]
    nums1_right_min = i == m ? Float::INFINITY : nums1[i]
    nums2_left_max = j.zero? ? -Float::INFINITY : nums2[j - 1]
    nums2_right_min = j == n ? Float::INFINITY : nums2[j]

    if nums1_left_max <= nums2_right_min && nums2_left_max <= nums1_right_min
      if (m + n).odd?
        return [nums1_left_max, nums2_left_max].max.to_f
      end
      return ([nums1_left_max, nums2_left_max].max + [nums1_right_min, nums2_right_min].min) / 2.0
    end

    if nums1_left_max > nums2_right_min
      hi = i - 1
    else
      lo = i + 1
    end
  end

  0.0
end
