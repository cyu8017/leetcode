// LeetCode 2040 - Kth Smallest Product of Two Sorted Arrays
// https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} k
 * @return {number}
 */
var kthSmallestProduct = function(nums1, nums2, k) {
    const countLE = (x) => {
        let cnt = 0;
        for (const a of nums1) {
            if (a > 0) {
                let lo = 0, hi = nums2.length;
                while (lo < hi) {
                    const mid = (lo + hi) >> 1;
                    if (a * nums2[mid] <= x) lo = mid + 1;
                    else hi = mid;
                }
                cnt += lo;
            } else if (a < 0) {
                let lo = 0, hi = nums2.length;
                while (lo < hi) {
                    const mid = (lo + hi) >> 1;
                    if (a * nums2[mid] <= x) hi = mid;
                    else lo = mid + 1;
                }
                cnt += nums2.length - lo;
            } else if (x >= 0) cnt += nums2.length;
        }
        return cnt;
    };
    let lo = -10000000000, hi = 10000000000;
    while (lo < hi) {
        const mid = lo + Math.floor((hi - lo) / 2);
        if (countLE(mid) >= k) hi = mid;
        else lo = mid + 1;
    }
    return lo;
};
