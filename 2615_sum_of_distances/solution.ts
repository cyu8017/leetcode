// LeetCode 2615 - Sum of Distances
// https://leetcode.com/problems/sum-of-distances/

export function distance(nums: number[]): number[] {
    const n = nums.length;
    const ans = new Array(n).fill(0);
    const pos = new Map();
    for (let i = 0; i < n; ++i) {
        if (!pos.has(nums[i])) pos.set(nums[i], []);
        pos.get(nums[i]).push(i);
    }
    for (const idxs of pos.values()) {
        const m = idxs.length;
        const pref = new Array(m + 1).fill(0);
        for (let i = 0; i < m; ++i) pref[i + 1] = pref[i] + idxs[i];
        for (let j = 0; j < m; ++j) {
            const idx = idxs[j];
            const left = j * idx - pref[j];
            const right = pref[m] - pref[j + 1] - (m - 1 - j) * idx;
            ans[idx] = left + right;
        }
    }
    return ans;
}
