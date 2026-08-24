// LeetCode 0643 - Maximum Average Subarray I
// https://leetcode.com/problems/maximum-average-subarray-i/

export function findMaxAverage(nums: number[], k: number): number {
    let window = 0;
    for (let i = 0; i < k; ++i) window += nums[i];
    let best = window;
    for (let i = k; i < nums.length; ++i) {
        window += nums[i] - nums[i - k];
        best = Math.max(best, window);
    }
    return best / k;
}
