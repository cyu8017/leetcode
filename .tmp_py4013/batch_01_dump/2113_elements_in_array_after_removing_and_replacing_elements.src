// LeetCode 2113 - Elements in Array After Removing and Replacing Elements
// https://leetcode.com/problems/elements-in-array-after-removing-and-replacing-elements/

/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {number[]}
 */
var elementInNums = function(nums, queries) {
    const n = nums.length;
    const ans = new Array(queries.length);
    for (let i = 0; i < queries.length; i++) {
        const t = queries[i][0], idx = queries[i][1];
        const cycle = t % (2 * n);
        let size, offset;
        if (cycle < n) {
            size = n - cycle;
            offset = cycle;
        } else {
            size = cycle - n;
            offset = 0;
        }
        ans[i] = idx >= size ? -1 : nums[offset + idx];
    }
    return ans;
};
