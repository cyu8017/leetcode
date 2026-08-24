// LeetCode 0628 - Maximum Product of Three Numbers
// https://leetcode.com/problems/maximum-product-of-three-numbers/

export function maximumProduct(nums: number[]): number {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    return Math.max(nums[n - 1] * nums[n - 2] * nums[n - 3], nums[0] * nums[1] * nums[n - 1]);
}
