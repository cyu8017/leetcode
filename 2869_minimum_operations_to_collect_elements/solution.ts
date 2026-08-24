// LeetCode 2869 - Minimum Operations to Collect Elements
// https://leetcode.com/problems/minimum-operations-to-collect-elements/

export function minOperations(nums: number[], k: number): number {
    const need = new Set();
    for (let i = 1; i <= k; i++) need.add(i);
    for (let i = nums.length - 1; i >= 0; i--) {
        need.delete(nums[i]);
        if (need.size === 0) return nums.length - i;
    }
    return nums.length;
}
