// LeetCode 1221 - Split a String in Balanced Strings
// https://leetcode.com/problems/split-a-string-in-balanced-strings/

/**
 * @param {string} s
 * @return {number}
 */
var balancedStringSplit = function(s) {
    let balance = 0, answer = 0;
    for (const ch of s) {
        balance += ch === "L" ? 1 : -1;
        if (balance === 0) answer++;
    }
    return answer;
};
