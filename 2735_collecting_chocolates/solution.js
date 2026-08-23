// LeetCode 2735 - Collecting Chocolates
// https://leetcode.com/problems/collecting-chocolates/

/**
 * @param {number[]} nums
 * @param {number} x
 * @return {number}
 */
var minCost = function(nums, x) {
    const n = nums.length;
    const best = nums.slice();
    let ans = 0;
    for (const v of nums) ans += v;
    for (let rot = 1; rot < n; rot++) {
        let cur = rot * x;
        for (let i = 0; i < n; i++) {
            best[i] = Math.min(best[i], nums[(i + rot) % n]);
            cur += best[i];
        }
        ans = Math.min(ans, cur);
    }
    return ans;
};
