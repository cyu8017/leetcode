// LeetCode 2613 - Beautiful Pairs
// https://leetcode.com/problems/beautiful-pairs/

export function beautifulPair(nums1: number[], nums2: number[]): number[] {
    const n = nums1.length;
    let best = Infinity;
    let ans = [0, 1];
    for (let i = 0; i < n; ++i) {
        for (let j = i + 1; j < n; ++j) {
            const d = Math.abs(nums1[i] - nums1[j]) + Math.abs(nums2[i] - nums2[j]);
            if (d < best || (d === best && (i < ans[0] || (i === ans[0] && j < ans[1])))) {
                best = d;
                ans = [i, j];
            }
        }
    }
    return ans;
}
