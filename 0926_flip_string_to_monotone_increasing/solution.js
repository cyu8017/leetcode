// LeetCode 0926 - Flip String to Monotone Increasing
// https://leetcode.com/problems/flip-string-to-monotone-increasing/

/**
 * @param {string} s
 * @return {number}
 */
var minFlipsMonoIncr = function(s) {
    let ones = 0, ans = 0;
    for (const ch of s) {
        if (ch === "1") ones++;
        else ans = Math.min(ans + 1, ones);
    }
    return ans;
};
