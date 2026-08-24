// LeetCode 3422 - Minimum Operations to Make Subarray Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-subarray-elements-equal/

export function minOperations(nums: any, k: any): any {
    const n = nums.length;
    let ans = Number.MAX_SAFE_INTEGER;
    for (let i = 0; i + k <= n; i++) {
        const sub = nums.slice(i, i + k).sort((a, b) => a - b);
        const med = sub[Math.floor(k / 2)];
        let cost = 0;
        for (const x of sub) cost += Math.abs(x - med);
        if (cost < ans) ans = cost;
    }
    return ans;
}
