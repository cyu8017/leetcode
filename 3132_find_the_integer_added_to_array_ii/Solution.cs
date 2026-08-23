// LeetCode 3132 - Find the Integer Added to Array II
// https://leetcode.com/problems/find-the-integer-added-to-array-ii/

using System;

public class Solution {
    public int MinimumAddedInteger(int[] nums1, int[] nums2) {
        Array.Sort(nums1);
        Array.Sort(nums2);
        int ans = 1 << 30;
        bool F(int x) {
            int i = 0, j = 0, cnt = 0;
            while (i < nums1.Length && j < nums2.Length) {
                if (nums2[j] - nums1[i] != x) cnt++;
                else j++;
                i++;
            }
            return cnt <= 2;
        }
        for (int t = 0; t < 3; t++) {
            int x = nums2[0] - nums1[t];
            if (F(x)) ans = Math.Min(ans, x);
        }
        return ans;
    }
}
