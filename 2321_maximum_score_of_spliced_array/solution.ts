// LeetCode 2321 - Maximum Score Of Spliced Array
// https://leetcode.com/problems/maximum-score-of-spliced-array/

export function maximumsSplicedArray(nums1: number[], nums2: number[]): number {
    const kadane = (a, b) => {
        let best = 0, cur = 0, sum = 0;
        for (let i = 0; i < a.length; ++i) {
            sum += a[i];
            cur += b[i] - a[i];
            if (cur < 0) cur = 0;
            best = Math.max(best, cur);
        }
        return sum + best;
    };
    return Math.max(kadane(nums1, nums2), kadane(nums2, nums1));
}
