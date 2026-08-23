// LeetCode 3152 - Special Array II
// https://leetcode.com/problems/special-array-ii/

/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {boolean[]}
 */
var isArraySpecial = function(nums, queries) {
    const n = nums.length;
    const d = new Array(n);
    for (let i = 0; i < n; i++) d[i] = i;
    for (let i = 1; i < n; i++) {
        if (nums[i] % 2 !== nums[i - 1] % 2) d[i] = d[i - 1];
    }
    const ans = new Array(queries.length);
    for (let i = 0; i < queries.length; i++)
        ans[i] = d[queries[i][1]] <= queries[i][0];
    return ans;
};
