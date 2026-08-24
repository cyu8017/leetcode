// LeetCode 3105 - Longest Strictly Increasing or Strictly Decreasing Subarray
// https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

export function longestMonotonicSubarray(nums: number[]): number {
    let ans = 1, t = 1;
    for (let i = 1; i < nums.length; i++) {
        if (nums[i - 1] < nums[i]) {
            t++;
            ans = Math.max(ans, t);
        } else t = 1;
    }
    t = 1;
    for (let i = 1; i < nums.length; i++) {
        if (nums[i - 1] > nums[i]) {
            t++;
            ans = Math.max(ans, t);
        } else t = 1;
    }
    return ans;
}
