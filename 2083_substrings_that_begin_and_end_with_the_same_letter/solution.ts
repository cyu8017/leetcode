// LeetCode 2083 - Substrings That Begin and End With the Same Letter
// https://leetcode.com/problems/substrings-that-begin-and-end-with-the-same-letter/

export function numberOfSubstrings(s: string): number {
    const freq = new Array(26).fill(0);
    let ans = 0;
    for (const c of s) {
        freq[c.charCodeAt(0) - 97]++;
        ans += freq[c.charCodeAt(0) - 97];
    }
    return ans;
}
