// LeetCode 2733 - Neither Minimum nor Maximum
// https://leetcode.com/problems/neither-minimum-nor-maximum/

export function findNonMinOrMax(nums: number[]): number {
    if (nums.length < 3) return -1;
    const a = nums[0], b = nums[1], c = nums[2];
    return a + b + c - Math.max(a, b, c) - Math.min(a, b, c);
}
