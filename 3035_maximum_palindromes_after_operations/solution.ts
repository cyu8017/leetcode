// LeetCode 3035 - Maximum Palindromes After Operations
// https://leetcode.com/problems/maximum-palindromes-after-operations/

function popcount(x: any): any {
    let c = 0;
    while (x !== 0) { c += x & 1; x >>= 1; }
    return c;
}export function maxPalindromesAfterOperations(words: any): any {
    let s = 0, mask = 0;
    for (const w of words) {
        s += w.length;
        for (let i = 0; i < w.length; i++) mask ^= 1 << (w.charCodeAt(i) - 97);
    }
    s -= popcount(mask);
    words.sort((a, b) => a.length - b.length);
    let ans = 0;
    for (const w of words) {
        s -= ((w.length / 2) | 0) * 2;
        if (s < 0) break;
        ans++;
    }
    return ans;
}
