// LeetCode 2090 - K Radius Subarray Averages
// https://leetcode.com/problems/k-radius-subarray-averages/

export function getAverages(nums: number[], k: number): number[] {
    const n = nums.length;
    const ans = new Array(n).fill(-1);
    if (2 * k + 1 > n) return ans;
    let sum = 0;
    for (let i = 0; i < 2 * k + 1; i++) sum += nums[i];
    ans[k] = Math.floor(sum / (2 * k + 1));
    for (let i = k + 1; i + k < n; i++) {
        sum += nums[i + k] - nums[i - k - 1];
        ans[i] = Math.floor(sum / (2 * k + 1));
    }
    return ans;
}
