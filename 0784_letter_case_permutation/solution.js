// LeetCode 0784 - Letter Case Permutation
// https://leetcode.com/problems/letter-case-permutation/

/**
 * @param {string} s
 * @return {string[]}
 */
var letterCasePermutation = function(s) {
    let result = [""];
    for (const ch of s) {
        const next = [];
        if (/[a-zA-Z]/.test(ch)) {
            const lower = ch.toLowerCase();
            const upper = ch.toUpperCase();
            for (const prefix of result) {
                next.push(prefix + lower);
                next.push(prefix + upper);
            }
        } else {
            for (const prefix of result) next.push(prefix + ch);
        }
        result = next;
    }
    return result;
};
