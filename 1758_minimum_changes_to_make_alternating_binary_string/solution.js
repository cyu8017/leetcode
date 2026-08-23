// LeetCode 1758 - Minimum Changes To Make Alternating Binary String
// https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

/**
 * @param {string} s
 * @return {number}
 */
var minOperations = function(s) {
    let alt1 = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] !== ((i & 1) === 0 ? '0' : '1')) {
            alt1++;
        }
    }
    return Math.min(alt1, s.length - alt1);
};
