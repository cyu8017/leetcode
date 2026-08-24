// LeetCode 2068 - Check Whether Two Strings Are Almost Equivalent
// https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/

export function checkAlmostEquivalent(word1: string, word2: string): boolean {
    const freq = new Array(26).fill(0);
    for (let i = 0; i < word1.length; i++) {
        freq[word1.charCodeAt(i) - 97]++;
        freq[word2.charCodeAt(i) - 97]--;
    }
    for (const v of freq) if (v > 3 || v < -3) return false;
    return true;
}
