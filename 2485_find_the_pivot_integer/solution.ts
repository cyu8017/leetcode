// LeetCode 2485 - Find the Pivot Integer
// https://leetcode.com/problems/find-the-pivot-integer/

export function pivotInteger(n: number): number {
    const total = n * (n + 1) / 2;
    let sum = 0;
    for (let x = 1; x <= n; x++) {
        sum += x;
        if (sum === total - sum + x) return x;
    }
    return -1;
}
