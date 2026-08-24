// LeetCode 3828 - Final Element After Subarray Deletions
// https://leetcode.com/problems/final-element-after-subarray-deletions/

export function finalElement(nums: any): any {
    return Math.max(nums[0], nums[nums.length - 1]);
}
