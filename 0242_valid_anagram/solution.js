// LeetCode 0242 - Valid Anagram
// https://leetcode.com/problems/valid-anagram/

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if (s.length !== t.length) {
        return false;
    }
    const counts = new Array(26).fill(0);
    for (let index = 0; index < s.length; index++) {
        counts[s.charCodeAt(index) - 97]++;
        counts[t.charCodeAt(index) - 97]--;
    }
    return counts.every((count) => count === 0);
};
