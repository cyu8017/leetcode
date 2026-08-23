// LeetCode 3110 - Score of a String
// https://leetcode.com/problems/score-of-a-string/

/**
 * @param {string} s
 * @return {number}
 */
var scoreOfString = function(s) {
    let ans = 0;
    for (let i = 1; i < s.length; i++)
        ans += Math.abs(s.charCodeAt(i - 1) - s.charCodeAt(i));
    return ans;
};
