// LeetCode 0091 - Decode Ways
// https://leetcode.com/problems/decode-ways/

/**
 * @param {string} s
 * @return {number}
 */
var numDecodings = function(s) {
    if (!s || s[0] === '0') {
        return 0;
    }

    let prev2 = 1;
    let prev1 = 1;

    for (let i = 1; i < s.length; i++) {
        let current = 0;
        if (s[i] !== '0') {
            current += prev1;
        }
        const two = parseInt(s.substring(i - 1, i + 1), 10);
        if (two >= 10 && two <= 26) {
            current += prev2;
        }
        prev2 = prev1;
        prev1 = current;
    }

    return prev1;
};
