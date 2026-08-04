// LeetCode 1936 - Add Minimum Number of Rungs
// https://leetcode.com/problems/add-minimum-number-of-rungs/

/**
 * @param {number[]} rungs
 * @param {number} dist
 * @return {number}
 */
var addRungs = function(rungs, dist) {
    let prev = 0, ans = 0;
    for (const r of rungs) {
        ans += Math.floor((r - prev - 1) / dist);
        prev = r;
    }
    return ans;
};
