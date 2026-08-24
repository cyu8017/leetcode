// LeetCode 2206 - Divide Array Into Equal Pairs
// https://leetcode.com/problems/divide-array-into-equal-pairs/

export function divideArray(nums: number[]): boolean {
    const freq = new Map();
    for (const x of nums) freq.set(x, (freq.get(x) || 0) + 1);
    for (const c of freq.values()) if (c % 2 !== 0) return false;
    return true;
}
