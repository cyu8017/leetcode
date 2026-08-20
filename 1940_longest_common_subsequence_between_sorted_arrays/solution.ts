// LeetCode 1940 - Longest Common Subsequence Between Sorted Arrays
// https://leetcode.com/problems/longest-common-subsequence-between-sorted-arrays/

function longestCommonSubsequence(arrays: number[][]): number[] {
    const cnt = new Map();
    for (const arr of arrays) {
        for (const x of arr) cnt.set(x, (cnt.get(x) || 0) + 1);
    }
    const m = arrays.length;
    return arrays[0].filter((x: any) => cnt.get(x) === m);
}
