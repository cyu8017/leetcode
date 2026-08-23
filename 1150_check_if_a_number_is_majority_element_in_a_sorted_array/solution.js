// LeetCode 1150 - Check If a Number Is Majority Element in a Sorted Array
// https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {boolean}
 */
var isMajorityElement = function(nums, target) {
    const bisectLeft = (arr, x) => {
        let lo = 0, hi = arr.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (arr[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    };
    const bisectRight = (arr, x) => {
        let lo = 0, hi = arr.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (arr[mid] <= x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    };
    return bisectRight(nums, target) - bisectLeft(nums, target) > Math.floor(nums.length / 2);
};
