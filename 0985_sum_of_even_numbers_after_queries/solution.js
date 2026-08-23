// LeetCode 0985 - Sum of Even Numbers After Queries
// https://leetcode.com/problems/sum-of-even-numbers-after-queries/

/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {number[]}
 */
var sumEvenAfterQueries = function(nums, queries) {
    let even = 0;
    for (const x of nums) if (x % 2 === 0) even += x;
    const ans = new Array(queries.length);
    for (let qi = 0; qi < queries.length; qi++) {
        const val = queries[qi][0], i = queries[qi][1];
        if (nums[i] % 2 === 0) even -= nums[i];
        nums[i] += val;
        if (nums[i] % 2 === 0) even += nums[i];
        ans[qi] = even;
    }
    return ans;
};
