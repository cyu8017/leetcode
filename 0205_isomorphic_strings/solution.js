// LeetCode 0205 - Isomorphic Strings
// https://leetcode.com/problems/isomorphic-strings/

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    const forward = new Map();
    const reverse = new Map();

    for (let i = 0; i < s.length; i += 1) {
        const a = s[i];
        const b = t[i];
        if ((forward.has(a) && forward.get(a) !== b)
            || (reverse.has(b) && reverse.get(b) !== a)) {
            return false;
        }
        forward.set(a, b);
        reverse.set(b, a);
    }
    return true;
};