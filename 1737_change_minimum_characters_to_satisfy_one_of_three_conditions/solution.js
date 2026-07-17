// LeetCode 1737 - Change Minimum Characters to Satisfy One of Three Conditions
// https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/

/**
 * @param {string} a
 * @param {string} b
 * @return {number}
 */
var minCharacters = function(a, b) {
    const ca = new Array(26).fill(0);
    const cb = new Array(26).fill(0);
    for (const ch of a) {
        ca[ch.charCodeAt(0) - 97]++;
    }
    for (const ch of b) {
        cb[ch.charCodeAt(0) - 97]++;
    }
    const n = a.length;
    const m = b.length;
    let ans = n + m - Math.max(Math.max(...ca), Math.max(...cb));
    let preA = 0;
    let preB = 0;
    for (let code = 0; code < 25; code++) {
        preA += ca[code];
        preB += cb[code];
        ans = Math.min(ans, n - preA + preB, m - preB + preA);
    }
    return ans;
};
