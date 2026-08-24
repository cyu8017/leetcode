// LeetCode 3517 - Smallest Palindromic Rearrangement I
// https://leetcode.com/problems/smallest-palindromic-rearrangement-i/

export function smallestPalindrome(s: any): any {
    const cnt = new Array(26).fill(0);
    for (const c of s) cnt[c.charCodeAt(0) - 97]++;
    let t = '';
    let ch = '';
    for (let i = 0; i < 26; i++) {
        const c = String.fromCharCode(97 + i);
        const v = Math.floor(cnt[i] / 2);
        t += c.repeat(v);
        cnt[i] -= v * 2;
        if (cnt[i] === 1) ch = c;
    }
    let sb = t;
    if (ch) sb += ch;
    for (let i = t.length - 1; i >= 0; i--) sb += t[i];
    return sb;
}
