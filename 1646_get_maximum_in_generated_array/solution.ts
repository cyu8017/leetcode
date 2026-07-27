// LeetCode 1646 - Get Maximum in Generated Array
// https://leetcode.com/problems/get-maximum-in-generated-array/

function getMaximumGenerated(n: number): number {
    if (n < 2) return n;
    const a = Array(n + 1).fill(0);
    a[1] = 1;
    for (let i = 2; i <= n; i++) {
        a[i] = i % 2 === 0 ? a[i >> 1] : a[i >> 1] + a[(i >> 1) + 1];
    }
    return Math.max(...a);
}
