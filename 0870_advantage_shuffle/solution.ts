// LeetCode 0870 - Advantage Shuffle
// https://leetcode.com/problems/advantage-shuffle/

export function advantageCount(nums1: number[], nums2: number[]): number[] {
    const sorted1 = nums1.slice().sort((a, b) => a - b);
    const dq = sorted1;
    let lo = 0, hi = dq.length - 1;
    const ans = new Array(nums1.length);
    const indexed = nums2.map((v, i) => [v, i]).sort((a, b) => b[0] - a[0]);
    for (const [val, i] of indexed) {
        if (dq[hi] > val) ans[i] = dq[hi--];
        else ans[i] = dq[lo++];
    }
    return ans;
}
