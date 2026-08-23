// LeetCode 2414 - Length of the Longest Alphabetical Continuous Substring
// https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/

/**
 * @param {string} s
 * @return {number}
 */
var longestContinuousSubstring = function(s) {
    let ans = 1, cur = 1;
    for (let i = 1; i < s.length; i++) {
        if (s.charCodeAt(i) === s.charCodeAt(i - 1) + 1) {
            cur++;
            ans = Math.max(ans, cur);
        } else {
            cur = 1;
        }
    }
    return ans;
};
