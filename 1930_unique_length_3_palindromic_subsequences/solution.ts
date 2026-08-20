// LeetCode 1930 - Unique Length-3 Palindromic Subsequences
// https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

function countPalindromicSubsequence(s: string): number {
    const first = new Map(), last = new Map();
    for (let i = 0; i < s.length; i++) {
        if (!first.has(s[i])) first.set(s[i], i);
        last.set(s[i], i);
    }
    let ans = 0;
    for (const [c, f] of first) {
        const l = last.get(c);
        if (l - f > 1) ans += new Set(s.slice(f + 1, l)).size;
    }
    return ans;
}
