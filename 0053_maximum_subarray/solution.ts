// LeetCode 0053 - Maximum Subarray
// https://leetcode.com/problems/maximum-subarray/

export function maxSubArray(nums: number[]): number {
    let best = nums[0];
    let current = nums[0];

    for (let i = 1; i < nums.length; i++) {
        current = Math.max(nums[i], current + nums[i]);
        best = Math.max(best, current);
    }

    return best;
}
