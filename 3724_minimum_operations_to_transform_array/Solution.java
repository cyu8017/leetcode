// LeetCode 3724 - Minimum Operations to Transform Array
// https://leetcode.com/problems/minimum-operations-to-transform-array/

class Solution {
    public long minOperations(int[] nums1, int[] nums2) {
        long ans = 1;
        int n = nums1.length;
        boolean ok = false;
        int d = 1 << 30;
        for (int i = 0; i < n; i++) {
            int x = Math.max(nums1[i], nums2[i]);
            int y = Math.min(nums1[i], nums2[i]);
            ans += x - y;
            d = Math.min(d, Math.min(Math.abs(x - nums2[n]), Math.abs(y - nums2[n])));
            if (nums2[n] >= y && nums2[n] <= x) ok = true;
        }
        if (!ok) ans += d;
        return ans;
    }
}
