// LeetCode 0908 - Smallest Range I
// https://leetcode.com/problems/smallest-range-i/

export function smallestRangeI(nums: number[], k: number): number {
    let mn = nums[0], mx = nums[0];
    for (const x of nums) {
        mn = Math.min(mn, x);
        mx = Math.max(mx, x);
    }
    return Math.max(0, mx - mn - 2 * k);
}
