// LeetCode 2343 - Query Kth Smallest Trimmed Number
// https://leetcode.com/problems/query-kth-smallest-trimmed-number/

/**
 * @param {string[]} nums
 * @param {number[][]} queries
 * @return {number[]}
 */
var smallestTrimmedNumbers = function(nums, queries) {
    const n = nums.length, m = queries.length;
    const ans = Array(m);
    for (let qi = 0; qi < m; qi++) {
        const k = queries[qi][0], trim = queries[qi][1];
        const arr = [];
        for (let i = 0; i < n; i++) {
            const s = nums[i];
            arr.push([s.substring(s.length - trim), i]);
        }
        arr.sort((a, b) => {
            if (a[0] !== b[0]) return a[0] < b[0] ? -1 : 1;
            return a[1] - b[1];
        });
        ans[qi] = arr[k - 1][1];
    }
    return ans;
};
