// LeetCode 1691 - Maximum Height by Stacking Cuboids
// https://leetcode.com/problems/maximum-height-by-stacking-cuboids/

function maxHeight(cuboids: number[][]): number {
    const a = cuboids.map((x) => [...x].sort((p, q) => p - q));
    a.sort((x, y) => {
        for (let d = 0; d < 3; d++) {
            if (x[d] !== y[d]) return x[d] - y[d];
        }
        return 0;
    });
    const n = a.length;
    const dp = Array(n).fill(0);
    for (let i = 0; i < n; i++) {
        dp[i] = a[i][2];
        for (let j = 0; j < i; j++) {
            if (a[j].every((v, d) => v <= a[i][d])) dp[i] = Math.max(dp[i], dp[j] + a[i][2]);
        }
    }
    return Math.max(...dp);
}
