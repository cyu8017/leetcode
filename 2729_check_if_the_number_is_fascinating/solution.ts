// LeetCode 2729 - Check if The Number is Fascinating
// https://leetcode.com/problems/check-if-the-number-is-fascinating/

export function isFascinating(n: number): boolean {
    const s = String(n) + String(2 * n) + String(3 * n);
    if (s.length !== 9) return false;
    const cnt = Array(10).fill(0);
    for (const c of s) cnt[c.charCodeAt(0) - 48]++;
    if (cnt[0] !== 0) return false;
    for (let i = 1; i <= 9; i++) if (cnt[i] !== 1) return false;
    return true;
}
