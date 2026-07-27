// LeetCode 1657 - Determine if Two Strings Are Close
// https://leetcode.com/problems/determine-if-two-strings-are-close/

function closeStrings(word1: string, word2: string): boolean {
    if (word1.length !== word2.length) return false;
    const count = (s: string): number[] => {
        const c = Array(26).fill(0);
        for (const ch of s) c[ch.charCodeAt(0) - 97]++;
        return c;
    };
    const a = count(word1), b = count(word2);
    for (let i = 0; i < 26; i++) {
        if ((a[i] === 0) !== (b[i] === 0)) return false;
    }
    a.sort((x, y) => x - y);
    b.sort((x, y) => x - y);
    return a.every((v, i) => v === b[i]);
}
