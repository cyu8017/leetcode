// LeetCode 1749 - Maximum Absolute Sum of Any Subarray
// https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

function maxAbsoluteSum(nums: number[]): number {
    let prefix = 0;
    let low = 0;
    let high = 0;
    for (const value of nums) {
        prefix += value;
        low = Math.min(low, prefix);
        high = Math.max(high, prefix);
    }
    return high - low;
}
