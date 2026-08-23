// LeetCode 3724 - Minimum Operations to Transform Array
// https://leetcode.com/problems/minimum-operations-to-transform-array/

using System;

public class Solution {
    public long MinOperations(int[] nums1, int[] nums2) {
        long ans = 1;
        int n = nums1.Length;
        bool ok = false;
        int d = 1 << 30;
        for (int i = 0; i < n; i++) {
            int x = Math.Max(nums1[i], nums2[i]);
            int y = Math.Min(nums1[i], nums2[i]);
            ans += x - y;
            d = Math.Min(d, Math.Min(Math.Abs(x - nums2[n]), Math.Abs(y - nums2[n])));
            if (nums2[n] >= y && nums2[n] <= x) ok = true;
        }
        if (!ok) ans += d;
        return ans;
    }
}
