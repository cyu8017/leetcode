// LeetCode 1624 - Largest Substring Between Two Equal Characters
// https://leetcode.com/problems/largest-substring-between-two-equal-characters/

/**
 * @param {string} s
 * @return {number}
 */
var maxLengthBetweenEqualCharacters = function(s) {
    const first = new Map();
    let ans = -1;
    for (let i = 0; i < s.length; i++) {
        if (first.has(s[i])) ans = Math.max(ans, i - first.get(s[i]) - 1);
        else first.set(s[i], i);
    }
    return ans;
};
