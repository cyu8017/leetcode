// LeetCode 1818 - Minimum Absolute Sum Difference
// https://leetcode.com/problems/minimum-absolute-sum-difference/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var minAbsoluteSumDiff = function(nums1, nums2) {
    const MOD = 1e9 + 7;
    const sorted = [...nums1].sort((a, b) => a - b);
    let total = 0;
    for (let i = 0; i < nums1.length; i++) total += Math.abs(nums1[i] - nums2[i]);
    let bestGain = 0;

    const bisectLeft = (arr, target) => {
        let lo = 0, hi = arr.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (arr[mid] < target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    };

    for (let i = 0; i < nums2.length; i++) {
        const target = nums2[i];
        const current = Math.abs(nums1[i] - target);
        const idx = bisectLeft(sorted, target);
        for (const j of [idx - 1, idx]) {
            if (j >= 0 && j < sorted.length) {
                bestGain = Math.max(bestGain, current - Math.abs(sorted[j] - target));
            }
        }
    }
    return (total - bestGain) % MOD;
};
