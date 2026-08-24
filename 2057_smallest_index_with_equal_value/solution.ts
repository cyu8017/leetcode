// LeetCode 2057 - Smallest Index With Equal Value
// https://leetcode.com/problems/smallest-index-with-equal-value/

export function smallestEqual(nums: number[]): number {
    for (let i = 0; i < nums.length; i++)
        if (i % 10 === nums[i]) return i;
    return -1;
}
