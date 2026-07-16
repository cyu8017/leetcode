// LeetCode 0034 - Find First and Last Position of Element in Sorted Array
// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

export function searchRange(nums: number[], target: number): number[] {
    function lowerBound(): number {
        let left = 0;
        let right = nums.length;
        while (left < right) {
            const mid = Math.floor((left + right) / 2);
            if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }

    function upperBound(): number {
        let left = 0;
        let right = nums.length;
        while (left < right) {
            const mid = Math.floor((left + right) / 2);
            if (nums[mid] <= target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }

    if (nums.length === 0) {
        return [-1, -1];
    }

    const start = lowerBound();
    if (start === nums.length || nums[start] !== target) {
        return [-1, -1];
    }

    return [start, upperBound() - 1];
}
