// LeetCode 0154 - Find Minimum in Rotated Sorted Array II
// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

export function findMin(nums: number[]): number {
    let left = 0;
    let right = nums.length - 1;

    while (left < right) {
        const middle = Math.floor((left + right) / 2);
        if (nums[middle] > nums[right]) {
            left = middle + 1;
        } else if (nums[middle] < nums[right]) {
            right = middle;
        } else {
            right -= 1;
        }
    }

    return nums[left];
}