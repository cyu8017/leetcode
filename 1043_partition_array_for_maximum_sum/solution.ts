// LeetCode 1043 - Partition Array for Maximum Sum
// https://leetcode.com/problems/partition-array-for-maximum-sum/

function maxSumAfterPartitioning(arr: number[], k: number): number {
    const n = arr.length;
    const dp = new Array(n + 1).fill(0);
    for (let i = 1; i <= n; i++) {
        let best = 0;
        for (let size = 1; size <= Math.min(k, i); size++) {
            best = Math.max(best, arr[i - size]);
            dp[i] = Math.max(dp[i], dp[i - size] + best * size);
        }
    }
    return dp[n];
}
