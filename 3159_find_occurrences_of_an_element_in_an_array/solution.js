// LeetCode 3159 - Find Occurrences of an Element in an Array
// https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/

/**
 * @param {number[]} nums
 * @param {number[]} queries
 * @param {number} x
 * @return {number[]}
 */
var occurrencesOfElement = function(nums, queries, x) {
    const ids = [];
    for (let i = 0; i < nums.length; i++) if (nums[i] === x) ids.push(i);
    const ans = new Array(queries.length);
    for (let qi = 0; qi < queries.length; qi++) {
        const i = queries[qi];
        if (i - 1 < ids.length) ans[qi] = ids[i - 1];
        else ans[qi] = -1;
    }
    return ans;
};
