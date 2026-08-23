// LeetCode 2546 - Apply Bitwise Operations to Make Strings Equal
// https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/

/**
 * @param {string} s
 * @param {string} target
 * @return {boolean}
 */
var makeStringsEqual = function(s, target) {
    let has1s = false, has1t = false;
    for (let i = 0; i < s.length; ++i) {
        if (s[i] === '1') has1s = true;
        if (target[i] === '1') has1t = true;
    }
    return has1s === has1t;
};
