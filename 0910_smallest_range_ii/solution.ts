// LeetCode 0910 - Smallest Range II
// https://leetcode.com/problems/smallest-range-ii/

export function smallestRangeII(nums: number[], k: number): number {
    nums.sort((a, b) => a - b);
    let ans = nums[nums.length - 1] - nums[0];
    for (let i = 0; i + 1 < nums.length; i++) {
        const lo = Math.min(nums[0] + k, nums[i + 1] - k);
        const hi = Math.max(nums[nums.length - 1] - k, nums[i] + k);
        ans = Math.min(ans, hi - lo);
    }
    return ans;
}
