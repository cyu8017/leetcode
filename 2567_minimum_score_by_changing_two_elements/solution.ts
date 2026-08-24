// LeetCode 2567 - Minimum Score by Changing Two Elements
// https://leetcode.com/problems/minimum-score-by-changing-two-elements/

export function minimizeSum(nums: number[]): number {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    return Math.min(nums[n - 1] - nums[2], nums[n - 3] - nums[0], nums[n - 2] - nums[1]);
}
