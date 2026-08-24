// LeetCode 3146 - Permutation Difference between Two Strings
// https://leetcode.com/problems/permutation-difference-between-two-strings/

export function findPermutationDifference(s: string, t: string): number {
    const d = new Array(26);
    for (let i = 0; i < s.length; i++) d[s.charCodeAt(i) - 97] = i;
    let ans = 0;
    for (let i = 0; i < t.length; i++) ans += Math.abs(d[t.charCodeAt(i) - 97] - i);
    return ans;
}
