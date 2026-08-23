// LeetCode 0004 - Median of Two Sorted Arrays
// https://leetcode.com/problems/median-of-two-sorted-arrays/

public class Solution {
    public double FindMedianSortedArrays(int[] nums1, int[] nums2) {
        if (nums1.Length > nums2.Length) {
            (nums1, nums2) = (nums2, nums1);
        }

        int m = nums1.Length;
        int n = nums2.Length;
        int totalLeft = (m + n + 1) / 2;
        int lo = 0;
        int hi = m;

        while (lo <= hi) {
            int i = (lo + hi) / 2;
            int j = totalLeft - i;

            int nums1LeftMax = i == 0 ? int.MinValue : nums1[i - 1];
            int nums1RightMin = i == m ? int.MaxValue : nums1[i];
            int nums2LeftMax = j == 0 ? int.MinValue : nums2[j - 1];
            int nums2RightMin = j == n ? int.MaxValue : nums2[j];

            if (nums1LeftMax <= nums2RightMin && nums2LeftMax <= nums1RightMin) {
                if ((m + n) % 2 == 1) {
                    return Math.Max(nums1LeftMax, nums2LeftMax);
                }
                return (Math.Max(nums1LeftMax, nums2LeftMax) + Math.Min(nums1RightMin, nums2RightMin)) / 2.0;
            }

            if (nums1LeftMax > nums2RightMin) {
                hi = i - 1;
            } else {
                lo = i + 1;
            }
        }

        return 0.0;
    }
}
