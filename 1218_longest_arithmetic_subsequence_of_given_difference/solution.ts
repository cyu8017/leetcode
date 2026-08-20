// LeetCode 1218 - Longest Arithmetic Subsequence of Given Difference
// https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

function longestSubsequence(arr: number[], difference: number): number {
    const dp = new Map();
    let best = 0;
    for (const x of arr) {
        const v = (dp.get(x - difference) || 0) + 1;
        dp.set(x, v);
        best = Math.max(best, v);
    }
    return best;
}
