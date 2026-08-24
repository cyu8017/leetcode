// LeetCode 2315 - Count Asterisks
// https://leetcode.com/problems/count-asterisks/

/**
 * @param {string} s
 * @return {number}
 */
var countAsterisks = function(s) {
    let ans = 0, inside = false;
    for (const c of s) {
        if (c === '|') inside = !inside;
        else if (c === '*' && !inside) ans++;
    }
    return ans;
};
