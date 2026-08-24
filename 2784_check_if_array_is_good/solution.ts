// LeetCode 2784 - Check if Array is Good
// https://leetcode.com/problems/check-if-array-is-good/

export function isGood(nums: number[]): boolean {
    const n = nums.length - 1;
    if (n < 1) return false;
    const freq = Array(n + 1).fill(0);
    for (const v of nums) {
        if (v < 1 || v > n) return false;
        freq[v]++;
    }
    for (let i = 1; i < n; i++) if (freq[i] !== 1) return false;
    return freq[n] === 2;
}
