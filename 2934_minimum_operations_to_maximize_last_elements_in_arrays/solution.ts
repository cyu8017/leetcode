// LeetCode 2934 - Minimum Operations to Maximize Last Elements in Arrays
// https://leetcode.com/problems/minimum-operations-to-maximize-last-elements-in-arrays/

export function minOperations(nums1: number[], nums2: number[]): number {
    const calc = (a1, a2) => {
        const n = a1.length;
        let ops = 0;
        const last1 = a1[n - 1], last2 = a2[n - 1];
        for (let i = 0; i < n - 1; i++) {
            const x = a1[i], y = a2[i];
            if (x <= last1 && y <= last2) continue;
            if (y <= last1 && x <= last2) { ops++; continue; }
            return 1 << 30;
        }
        return ops;
    };
    const n = nums1.length;
    let ans = calc(nums1, nums2);
    const t = nums1[n - 1];
    nums1[n - 1] = nums2[n - 1];
    nums2[n - 1] = t;
    const cand = calc(nums1, nums2) + 1;
    if (cand < ans) ans = cand;
    // restore
    nums2[n - 1] = nums1[n - 1];
    nums1[n - 1] = t;
    return ans >= (1 << 30) ? -1 : ans;
}
