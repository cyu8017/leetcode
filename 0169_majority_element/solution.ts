// LeetCode 0169 - Majority Element
// https://leetcode.com/problems/majority-element/

export function majorityElement(nums: number[]): number {
    let candidate = nums[0];
    let count = 0;

    for (const number of nums) {
        if (count === 0) {
            candidate = number;
        }
        count += number === candidate ? 1 : -1;
    }
    return candidate;
}