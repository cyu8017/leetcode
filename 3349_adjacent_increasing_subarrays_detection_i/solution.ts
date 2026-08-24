// LeetCode 3349 - Adjacent Increasing Subarrays Detection I
// https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/

function inc(nums: any, start: any, k: any): any {
    for (let i = start; i + 1 < start + k; i++) {
        if (nums[i] >= nums[i + 1]) return false;
    }
    return true;
}export function hasIncreasingSubarrays(nums: any, k: any): any {
    const n = nums.length;
    for (let i = 0; i + 2 * k <= n; i++) {
        if (inc(nums, i, k) && inc(nums, i + k, k)) return true;
    }
    return false;
}
