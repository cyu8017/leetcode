// LeetCode 0828 - Count Unique Characters of All Substrings of a Given String
// https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/

/**
 * @param {string} s
 * @return {number}
 */
var uniqueLetterString = function(s) {
    const n = s.length;
    const last = new Map();
    for (const ch of s) {
        if (!last.has(ch)) last.set(ch, [-1]);
    }
    for (let i = 0; i < n; i++) last.get(s[i]).push(i);
    for (const indices of last.values()) indices.push(n);
    let ans = 0;
    for (const indices of last.values()) {
        for (let k = 1; k + 1 < indices.length; k++) {
            ans += (indices[k] - indices[k - 1]) * (indices[k + 1] - indices[k]);
        }
    }
    return ans;
};
