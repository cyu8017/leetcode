// LeetCode 2124 - Check if All A's Appears Before All B's
// https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/

/**
 * @param {string} s
 * @return {boolean}
 */
var checkString = function(s) {
    let seenB = false;
    for (let i = 0; i < s.length; i++) {
        const c = s[i];
        if (c === 'b') seenB = true;
        else if (seenB) return false;
    }
    return true;
};
