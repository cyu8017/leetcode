// LeetCode 2870 - Minimum Number of Operations to Make Array Empty
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/

export function minOperations(nums: number[]): number {
    const freq = new Map();
    for (const v of nums) freq.set(v, (freq.get(v) || 0) + 1);
    let ans = 0;
    for (const c of freq.values()) {
        if (c === 1) return -1;
        ans += Math.floor((c + 2) / 3);
    }
    return ans;
}
