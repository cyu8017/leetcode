// LeetCode 0152 - Maximum Product Subarray
// https://leetcode.com/problems/maximum-product-subarray/

export function maxProduct(nums: number[]): number {
    let best = nums[0];
    let currentMax = nums[0];
    let currentMin = nums[0];

    for (let index = 1; index < nums.length; index += 1) {
        const value = nums[index];
        const previousMax = currentMax;
        currentMax = Math.max(value, previousMax * value, currentMin * value);
        currentMin = Math.min(value, previousMax * value, currentMin * value);
        best = Math.max(best, currentMax);
    }

    return best;
}