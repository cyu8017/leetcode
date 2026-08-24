// LeetCode 2309 - Greatest English Letter in Upper and Lower Case
// https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/

export function greatestLetter(s: string): string {
    const lower = Array(26).fill(false), upper = Array(26).fill(false);
    for (const c of s) {
        if (c >= 'a' && c <= 'z') lower[c.charCodeAt(0) - 97] = true;
        else upper[c.charCodeAt(0) - 65] = true;
    }
    for (let i = 25; i >= 0; --i)
        if (lower[i] && upper[i]) return String.fromCharCode(65 + i);
    return "";
}
