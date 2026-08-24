// LeetCode 3674 - Minimum Operations to Equalize Array
// https://leetcode.com/problems/minimum-operations-to-equalize-array/

export function minOperations(nums: any): any {
    for (const x of nums) if (x !== nums[0]) return 1;
    return 0;
}
