// LeetCode 1513 - Number of Substrings With Only 1s
// https://leetcode.com/problems/number-of-substrings-with-only-1s/

/**
 * @param {string} s
 * @return {number}
 */
var numSub = function(s) {
    let ans = 0, run = 0;
    for (const ch of s) {
        run = ch === "1" ? run + 1 : 0;
        ans += run;
    }
    return ans % 1000000007;
};
