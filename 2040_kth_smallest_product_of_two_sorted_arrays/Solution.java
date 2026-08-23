// LeetCode 2040 - Kth Smallest Product of Two Sorted Arrays
// https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/

class Solution {
    public long kthSmallestProduct(int[] nums1, int[] nums2, long k) {
        long lo = -10_000_000_000L, hi = 10_000_000_000L;
        while (lo < hi) {
            long mid = lo + (hi - lo) / 2;
            if (countLE(nums1, nums2, mid) >= k) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    private long countLE(int[] nums1, int[] nums2, long x) {
        long cnt = 0;
        for (int a : nums1) {
            if (a > 0) {
                int lo = 0, hi = nums2.length;
                while (lo < hi) {
                    int mid = (lo + hi) / 2;
                    if ((long) a * nums2[mid] <= x) lo = mid + 1;
                    else hi = mid;
                }
                cnt += lo;
            } else if (a < 0) {
                int lo = 0, hi = nums2.length;
                while (lo < hi) {
                    int mid = (lo + hi) / 2;
                    if ((long) a * nums2[mid] <= x) hi = mid;
                    else lo = mid + 1;
                }
                cnt += nums2.length - lo;
            } else if (x >= 0) cnt += nums2.length;
        }
        return cnt;
    }
}
