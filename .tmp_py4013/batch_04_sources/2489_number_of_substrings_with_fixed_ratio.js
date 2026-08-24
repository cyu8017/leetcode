// LeetCode 2489 - Number of Substrings With Fixed Ratio
// https://leetcode.com/problems/number-of-substrings-with-fixed-ratio/

/**
 * @param {string} s
 * @param {number} num1
 * @param {number} num2
 * @return {number}
 */
var fixedRatio = function(s, num1, num2) {
    const pref = new Map();
    pref.set(0, 1);
    let zeros = 0, ones = 0, ans = 0;
    for (const c of s) {
        if (c === '0') zeros++;
        else ones++;
        const key = zeros * num2 - ones * num1;
        ans += pref.get(key) || 0;
        pref.set(key, (pref.get(key) || 0) + 1);
    }
    return ans;
};
