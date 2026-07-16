// LeetCode 0540 - Single Element in a Sorted Array
// https://leetcode.com/problems/single-element-in-a-sorted-array/

export class Solution {
    singleNonDuplicate(nums: number[]): number {
        let left = 0;
        let right = nums.length - 1;

        while (left < right) {
            let mid = Math.floor((left + right) / 2);
            if (mid % 2 === 1) mid -= 1;
            if (nums[mid] === nums[mid + 1]) {
                left = mid + 2;
            } else {
                right = mid;
            }
        }
        return nums[left];
    }
}
