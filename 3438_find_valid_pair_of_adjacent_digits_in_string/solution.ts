// LeetCode 3438 - Find Valid Pair of Adjacent Digits in String
// https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/

export function findValidPair(s: any): any {
    const freq = new Array(10).fill(0);
    for (const c of s) freq[c.charCodeAt(0) - 48]++;
    for (let i = 0; i + 1 < s.length; i++) {
        const a = s.charCodeAt(i) - 48, b = s.charCodeAt(i + 1) - 48;
        if (a !== b && freq[a] === a && freq[b] === b) return s.substring(i, i + 2);
    }
    return "";
}
