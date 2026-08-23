// LeetCode 0215 - Kth Largest Element in an Array
// https://leetcode.com/problems/kth-largest-element-in-an-array/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function(nums, k) {
    const target = nums.length - k;

    const partition = (left, right) => {
        const pivotIndex = left + Math.floor(Math.random() * (right - left + 1));
        [nums[pivotIndex], nums[right]] = [nums[right], nums[pivotIndex]];
        let store = left;
        for (let i = left; i < right; i += 1) {
            if (nums[i] <= nums[right]) {
                [nums[store], nums[i]] = [nums[i], nums[store]];
                store += 1;
            }
        }
        [nums[store], nums[right]] = [nums[right], nums[store]];
        return store;
    };

    let left = 0;
    let right = nums.length - 1;
    while (left <= right) {
        const pivotIndex = partition(left, right);
        if (pivotIndex === target) {
            return nums[pivotIndex];
        }
        if (pivotIndex < target) {
            left = pivotIndex + 1;
        } else {
            right = pivotIndex - 1;
        }
    }
    return nums[left];
};
