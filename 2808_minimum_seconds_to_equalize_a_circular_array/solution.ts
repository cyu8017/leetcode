// LeetCode 2808 - Minimum Seconds to Equalize a Circular Array
// https://leetcode.com/problems/minimum-seconds-to-equalize-a-circular-array/

export function minimumSeconds(nums: number[]): number {
    const n = nums.length;
    const pos = new Map();
    for (let i = 0; i < n; i++) {
        if (!pos.has(nums[i])) pos.set(nums[i], []);
        pos.get(nums[i]).push(i);
    }
    let ans = n;
    for (const p of pos.values()) {
        let maxGap = 0;
        for (let i = 0; i < p.length; i++) {
            const gap = (i + 1 < p.length) ? p[i + 1] - p[i] : p[0] + n - p[i];
            maxGap = Math.max(maxGap, Math.floor(gap / 2));
        }
        ans = Math.min(ans, maxGap);
    }
    return ans;
}
