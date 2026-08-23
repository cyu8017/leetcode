// LeetCode 0912 - Sort an Array
// https://leetcode.com/problems/sort-an-array/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArray = function(nums) {
    if (nums.length <= 1) return nums;
    const mid = nums.length >> 1;
    const left = sortArray(nums.slice(0, mid));
    const right = sortArray(nums.slice(mid));
    const merged = new Array(nums.length);
    let i = 0, j = 0, k = 0;
    while (i < left.length && j < right.length) {
        if (left[i] <= right[j]) merged[k++] = left[i++];
        else merged[k++] = right[j++];
    }
    while (i < left.length) merged[k++] = left[i++];
    while (j < right.length) merged[k++] = right[j++];
    return merged;
};
