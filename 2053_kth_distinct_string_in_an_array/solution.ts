// LeetCode 2053 - Kth Distinct String in an Array
// https://leetcode.com/problems/kth-distinct-string-in-an-array/

export function kthDistinct(arr: string[], k: number): string {
    const freq = new Map();
    for (const s of arr) freq.set(s, (freq.get(s) || 0) + 1);
    for (const s of arr) if (freq.get(s) === 1 && --k === 0) return s;
    return "";
}
