// LeetCode 1653 - Minimum Deletions to Make String Balanced
// https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

/**
 * @param {string} s
 * @return {number}
 */
var minimumDeletions = function(s) {
    let b = 0, ans = 0;
    for (const c of s) {
        if (c === "b") b++;
        else ans = Math.min(ans + 1, b);
    }
    return ans;
};
