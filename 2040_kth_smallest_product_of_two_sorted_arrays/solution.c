// LeetCode 2040 - Kth Smallest Product of Two Sorted Arrays
// https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/

static long long countLE2040(int* nums1, int n1, int* nums2, int n2, long long x) {
    long long cnt = 0;
    for (int i = 0; i < n1; i++) {
        int a = nums1[i];
        if (a > 0) {
            int lo = 0, hi = n2;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if ((long long)a * nums2[mid] <= x) lo = mid + 1;
                else hi = mid;
            }
            cnt += lo;
        } else if (a < 0) {
            int lo = 0, hi = n2;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if ((long long)a * nums2[mid] <= x) hi = mid;
                else lo = mid + 1;
            }
            cnt += n2 - lo;
        } else if (x >= 0) cnt += n2;
    }
    return cnt;
}

long long kthSmallestProduct(int* nums1, int nums1Size, int* nums2, int nums2Size, long long k) {
    long long lo = -10000000000LL, hi = 10000000000LL;
    while (lo < hi) {
        long long mid = lo + (hi - lo) / 2;
        if (countLE2040(nums1, nums1Size, nums2, nums2Size, mid) >= k) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
