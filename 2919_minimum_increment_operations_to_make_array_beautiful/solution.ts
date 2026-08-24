// LeetCode 2919 - Minimum Increment Operations to Make Array Beautiful
// https://leetcode.com/problems/minimum-increment-operations-to-make-array-beautiful/

export function minIncrementOperations(nums: number[], k: number): number {
    let dp0 = 0, dp1 = 0, dp2 = 0;
    for (const v of nums) {
        const cost = v < k ? k - v : 0;
        const nd0 = cost + Math.min(dp0, dp1, dp2);
        dp0 = dp1;
        dp1 = dp2;
        dp2 = nd0;
    }
    return Math.min(dp0, dp1, dp2);
}
