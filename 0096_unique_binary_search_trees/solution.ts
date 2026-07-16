// LeetCode 0096 - Unique Binary Search Trees
// https://leetcode.com/problems/unique-binary-search-trees/

export function numTrees(n: number): number {
    const dp: number[] = new Array(n + 1).fill(0);
    dp[0] = 1;
    for (let nodes = 1; nodes <= n; nodes++) {
        for (let root = 1; root <= nodes; root++) {
            dp[nodes] += dp[root - 1] * dp[nodes - root];
        }
    }
    return dp[n];
}
