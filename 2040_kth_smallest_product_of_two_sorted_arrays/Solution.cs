// LeetCode 2040 - Kth Smallest Product of Two Sorted Arrays
// https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/

public class Solution {
    public long KthSmallestProduct(int[] nums1, int[] nums2, long k) {
        long CountLE(long x) {
            long cnt = 0;
            foreach (int a in nums1) {
                if (a > 0) {
                    int lo = 0, hi = nums2.Length;
                    while (lo < hi) {
                        int mid = (lo + hi) / 2;
                        if ((long)a * nums2[mid] <= x) lo = mid + 1;
                        else hi = mid;
                    }
                    cnt += lo;
                } else if (a < 0) {
                    int lo = 0, hi = nums2.Length;
                    while (lo < hi) {
                        int mid = (lo + hi) / 2;
                        if ((long)a * nums2[mid] <= x) hi = mid;
                        else lo = mid + 1;
                    }
                    cnt += nums2.Length - lo;
                } else if (x >= 0) cnt += nums2.Length;
            }
            return cnt;
        }
        long lo = -10000000000L, hi = 10000000000L;
        while (lo < hi) {
            long mid = lo + (hi - lo) / 2;
            if (CountLE(mid) >= k) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
}
