// LeetCode 1933 - Check if String Is Decomposable Into Value-Equal Substrings
// https://leetcode.com/problems/check-if-string-is-decomposable-into-value-equal-substrings/

/**
 * @param {string} s
 * @return {boolean}
 */
var isDecomposable = function(s) {
    const n = s.length;
    let i = 0, twos = 0;
    while (i < n) {
        let j = i;
        while (j < n && s[j] === s[i]) j++;
        const length = j - i;
        if (length % 3 === 1) return false;
        if (length % 3 === 2) {
            twos++;
            if (twos > 1) return false;
        }
        i = j;
    }
    return twos === 1;
};
