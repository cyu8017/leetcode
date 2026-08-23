// LeetCode 3084 - Count Substrings Starting and Ending with Given Character
// https://leetcode.com/problems/count-substrings-starting-and-ending-with-given-character/

/**
 * @param {string} s
 * @param {character} c
 * @return {number}
 */
var countSubstrings = function(s, c) {
    let cnt = 0;
    for (let i = 0; i < s.length; i++) if (s[i] === c) cnt++;
    return cnt * (cnt + 1) / 2;
};
