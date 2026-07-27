// LeetCode 1684 - Count the Number of Consistent Strings
// https://leetcode.com/problems/count-the-number-of-consistent-strings/

function countConsistentStrings(allowed: string, words: string[]): number {
    const a = new Set(allowed);
    return words.filter((w) => [...w].every((c) => a.has(c))).length;
}
