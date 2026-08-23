// LeetCode 2030 - Smallest K-Length Subsequence With Occurrences of a Letter
// https://leetcode.com/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter/

/**
 * @param {string} s
 * @param {number} k
 * @param {character} letter
 * @param {number} repetition
 * @return {string}
 */
var smallestSubsequence = function(s, k, letter, repetition) {
    const n = s.length;
    let remainLetter = 0;
    for (const c of s) if (c === letter) remainLetter++;
    let stack = "";
    let inStackLetter = 0;
    for (let i = 0; i < n; i++) {
        const ch = s[i];
        while (stack.length > 0 && ch < stack[stack.length - 1] && stack.length + n - i > k) {
            const top = stack[stack.length - 1];
            if (top === letter) {
                if (inStackLetter + remainLetter - 1 < repetition) break;
                inStackLetter--;
            }
            stack = stack.slice(0, -1);
        }
        if (stack.length < k) {
            if (ch === letter) { stack += ch; inStackLetter++; }
            else if (k - stack.length > repetition - inStackLetter) stack += ch;
        }
        if (ch === letter) remainLetter--;
    }
    return stack;
};
