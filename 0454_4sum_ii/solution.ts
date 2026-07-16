// LeetCode 0454 - 4Sum II
// https://leetcode.com/problems/4sum-ii/

export class Solution {
    fourSumCount(nums1: number[], nums2: number[], nums3: number[], nums4: number[]): number {
        const pairSums = new Map<number, number>();
        for (const a of nums1) {
            for (const b of nums2) {
                const sum = a + b;
                pairSums.set(sum, (pairSums.get(sum) || 0) + 1);
            }
        }
        let total = 0;
        for (const c of nums3) {
            for (const d of nums4) {
                total += pairSums.get(-(c + d)) || 0;
            }
        }
        return total;
    }
}
