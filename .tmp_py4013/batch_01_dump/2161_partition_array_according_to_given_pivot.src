// LeetCode 2161 - Partition Array According to Given Pivot
// https://leetcode.com/problems/partition-array-according-to-given-pivot/

/**
 * @param {number[]} nums
 * @param {number} pivot
 * @return {number[]}
 */
var pivotArray = function(nums, pivot) {
    const ans = new Array(nums.length);
    let i = 0;
    for (const x of nums) if (x < pivot) ans[i++] = x;
    for (const x of nums) if (x === pivot) ans[i++] = x;
    for (const x of nums) if (x > pivot) ans[i++] = x;
    return ans;
};
