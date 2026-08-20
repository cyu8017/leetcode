// LeetCode 1573 - Number of Ways to Split a String
// https://leetcode.com/problems/number-of-ways-to-split-a-string/
// @ts-nocheck

function numWays(s: string): number {
    const MOD = 1000000007;
    let ones = 0;
    for (const ch of s) if (ch === "1") ones++;
    if (ones % 3) return 0;
    if (ones === 0) {
        const gaps = s.length - 1;
        return Math.floor(gaps * (gaps - 1) / 2) % MOD;
    }
    const target = ones / 3;
    const positions = [];
    for (let i = 0; i < s.length; i++) if (s[i] === "1") positions.push(i);
    return ((positions[target] - positions[target - 1]) * (positions[2 * target] - positions[2 * target - 1])) % MOD;
}
