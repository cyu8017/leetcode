// LeetCode 0153 - Find Minimum in Rotated Sorted Array
// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

export function findMin(nums: number[]): number {
    let left = 0;
    let right = nums.length - 1;

    while (left < right) {
        const middle = Math.floor((left + right) / 2);
        if (nums[middle] > nums[right]) {
            left = middle + 1;
        } else {
            right = middle;
        }
    }

    return nums[left];
}