// LeetCode 1906 - Minimum Absolute Difference Queries
// https://leetcode.com/problems/minimum-absolute-difference-queries/

/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {number[]}
 */
var minDifference = function(nums, queries) {
    const n = nums.length;
    const pref = Array.from({ length: n + 1 }, () => new Array(101).fill(0));
    for (let i = 0; i < n; i++) {
        for (let v = 0; v < 101; v++) pref[i + 1][v] = pref[i][v];
        pref[i + 1][nums[i]]++;
    }
    const ans = [];
    for (const [left, right] of queries) {
        let prev = -1, best = Infinity;
        for (let value = 1; value <= 100; value++) {
            if (pref[right + 1][value] - pref[left][value] > 0) {
                if (prev !== -1) best = Math.min(best, value - prev);
                prev = value;
            }
        }
        ans.push(best === Infinity ? -1 : best);
    }
    return ans;
};
