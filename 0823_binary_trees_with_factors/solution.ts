// LeetCode 0823 - Binary Trees With Factors
// https://leetcode.com/problems/binary-trees-with-factors/

export function numFactoredBinaryTrees(arr: number[]): number {
    const MOD = 1000000007;
    arr.sort((a, b) => a - b);
    const index = new Map();
    for (let i = 0; i < arr.length; i++) index.set(arr[i], i);
    const dp = new Array(arr.length).fill(1);
    let ans = 0;
    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < i; j++) {
            if (arr[i] % arr[j] === 0) {
                const right = Math.floor(arr[i] / arr[j]);
                if (index.has(right)) {
                    dp[i] = (dp[i] + dp[j] * dp[index.get(right)]) % MOD;
                }
            }
        }
        ans = (ans + dp[i]) % MOD;
    }
    return ans;
}
