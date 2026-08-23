// LeetCode 3080 - Mark Elements on Array by Performing Queries
// https://leetcode.com/problems/mark-elements-on-array-by-performing-queries/

/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {number[]}
 */
var unmarkedSumArray = function(nums, queries) {
    const n = nums.length;
    let s = 0;
    for (const x of nums) s += x;
    const mark = new Array(n).fill(false);
    const arr = nums.map((v, i) => [v, i]);
    arr.sort((a, b) => a[0] !== b[0] ? a[0] - b[0] : a[1] - b[1]);
    const ans = new Array(queries.length);
    let j = 0;
    for (let qi = 0; qi < queries.length; qi++) {
        const index = queries[qi][0];
        let k = queries[qi][1];
        if (!mark[index]) {
            mark[index] = true;
            s -= nums[index];
        }
        for (; k > 0 && j < n; j++) {
            if (!mark[arr[j][1]]) {
                mark[arr[j][1]] = true;
                s -= arr[j][0];
                k--;
            }
        }
        ans[qi] = s;
    }
    return ans;
};
