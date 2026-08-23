// LeetCode 1525 - Number of Good Ways to Split a String
// https://leetcode.com/problems/number-of-good-ways-to-split-a-string/

/**
 * @param {string} s
 * @return {number}
 */
var numSplits = function(s) {
    const right = new Map();
    for (const ch of s) right.set(ch, (right.get(ch) || 0) + 1);
    const left = new Set();
    let answer = 0;
    for (let i = 0; i < s.length - 1; i++) {
        const ch = s[i];
        left.add(ch);
        right.set(ch, right.get(ch) - 1);
        if (right.get(ch) === 0) right.delete(ch);
        if (left.size === right.size) answer++;
    }
    return answer;
};
