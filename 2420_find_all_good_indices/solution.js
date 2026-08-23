// LeetCode 2420 - Find All Good Indices
// https://leetcode.com/problems/find-all-good-indices/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var goodIndices = function(nums, k) {
    const n = nums.length;
    const dec = Array(n), inc = Array(n);
    dec[0] = 1;
    for (let i = 1; i < n; i++)
        dec[i] = nums[i] <= nums[i - 1] ? dec[i - 1] + 1 : 1;
    inc[n - 1] = 1;
    for (let i = n - 2; i >= 0; i--)
        inc[i] = nums[i] <= nums[i + 1] ? inc[i + 1] + 1 : 1;
    const ans = [];
    for (let i = k; i < n - k; i++) {
        if (dec[i - 1] >= k && inc[i + 1] >= k) ans.push(i);
    }
    return ans;
};
