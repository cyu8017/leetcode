// LeetCode 3627 - Maximum Median Sum of Subsequences of Size 3
// https://leetcode.com/problems/maximum-median-sum-of-subsequences-of-size-3/

export function maximumMedianSum(nums: any): any {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    let ans = 0;
    for (let i = Math.floor(n / 3); i < n; i += 2) ans += nums[i];
    return ans;
}
