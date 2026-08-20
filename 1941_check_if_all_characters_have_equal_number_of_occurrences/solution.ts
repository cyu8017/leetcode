// LeetCode 1941 - Check if All Characters Have Equal Number of Occurrences
// https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/

function areOccurrencesEqual(s: string): boolean {
    const freq = new Map();
    for (const c of s) freq.set(c, (freq.get(c) || 0) + 1);
    return new Set(freq.values()).size === 1;
}
