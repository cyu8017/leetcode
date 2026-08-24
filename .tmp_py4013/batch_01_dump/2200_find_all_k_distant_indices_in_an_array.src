// LeetCode 2200 - Find All K-Distant Indices in an Array
// https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

/**
 * @param {number[]} nums
 * @param {number} key
 * @param {number} k
 * @return {number[]}
 */
var findKDistantIndices = function(nums, key, k) {
    const n = nums.length;
    const mark = new Array(n).fill(false);
    for (let i = 0; i < n; i++) {
        if (nums[i] === key) {
            const l = Math.max(0, i - k), r = Math.min(n - 1, i + k);
            for (let j = l; j <= r; j++) mark[j] = true;
        }
    }
    const ans = [];
    for (let i = 0; i < n; i++) if (mark[i]) ans.push(i);
    return ans;
};
