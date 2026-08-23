// LeetCode 2222 - Number of Ways to Select Buildings
// https://leetcode.com/problems/number-of-ways-to-select-buildings/

/**
 * @param {string} s
 * @return {number}
 */
var numberOfWays = function(s) {
    let total0 = 0, total1 = 0;
    for (const c of s) {
        if (c === '0') total0++;
        else total1++;
    }
    let left0 = 0, left1 = 0, ans = 0;
    for (const c of s) {
        if (c === '0') {
            ans += left1 * (total1 - left1);
            left0++;
        } else {
            ans += left0 * (total0 - left0);
            left1++;
        }
    }
    return ans;
};
