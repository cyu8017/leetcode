// LeetCode 0217 - Contains Duplicate
// https://leetcode.com/problems/contains-duplicate/

export function containsDuplicate(nums: number[]): boolean {
    return new Set(nums).size !== nums.length;
}
