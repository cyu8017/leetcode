// LeetCode 2496 - Maximum Value of a String in an Array
// https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/

/**
 * @param {string[]} strs
 * @return {number}
 */
var maximumValue = function(strs) {
    let ans = 0;
    for (const s of strs) {
        let allDigit = true, val = 0;
        for (const c of s) {
            if (c < '0' || c > '9') { allDigit = false; break; }
            val = val * 10 + (c.charCodeAt(0) - 48);
        }
        if (!allDigit) val = s.length;
        if (val > ans) ans = val;
    }
    return ans;
};
