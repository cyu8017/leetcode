// LeetCode 2541 - Minimum Operations to Make Array Equal II
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii/

export function minOperations(nums1: number[], nums2: number[], k: number): number {
    if (k === 0) {
        for (let i = 0; i < nums1.length; i++) {
            if (nums1[i] !== nums2[i]) return -1;
        }
        return 0;
    }
    let pos = 0, neg = 0;
    for (let i = 0; i < nums1.length; i++) {
        const d = nums1[i] - nums2[i];
        if (d % k !== 0) return -1;
        if (d > 0) pos += d / k;
        else neg += (-d) / k;
    }
    return pos !== neg ? -1 : pos;
}
