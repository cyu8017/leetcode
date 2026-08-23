// LeetCode 2186 - Minimum Number of Steps to Make Two Strings Anagram II
// https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/

/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
var minSteps = function(s, t) {
    const freq = new Array(26).fill(0);
    for (let i = 0; i < s.length; i++) freq[s.charCodeAt(i) - 97]++;
    for (let i = 0; i < t.length; i++) freq[t.charCodeAt(i) - 97]--;
    let ans = 0;
    for (const v of freq) ans += Math.abs(v);
    return ans;
};
