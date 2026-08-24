// LeetCode 3810 - Minimum Operations To Reach Target Array
// https://leetcode.com/problems/minimum-operations-to-reach-target-array/

export function minOperations(nums: any, target: any): any {
    const s = new Set();
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== target[i]) s.add(nums[i]);
    }
    return s.size;
}
