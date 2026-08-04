// LeetCode 1966 - Binary Searchable Numbers in an Unsorted Array
// https://leetcode.com/problems/binary-searchable-numbers-in-an-unsorted-array/

/**
 * @param {number[]} nums
 * @return {number}
 */
var binarySearchableNumbers = function(nums) {
    const n = nums.length;
    const ok = new Array(n).fill(1);
    let mx = -Infinity, mi = Infinity;
    for (let i = 0; i < n; i++) {
        if (nums[i] < mx) ok[i] = 0;
        else mx = nums[i];
    }
    for (let i = n - 1; i >= 0; i--) {
        if (nums[i] > mi) ok[i] = 0;
        else mi = nums[i];
    }
    return ok.reduce((a, b) => a + b, 0);
};
