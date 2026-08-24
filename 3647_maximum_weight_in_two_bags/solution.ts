// LeetCode 3647 - Maximum Weight in Two Bags
// https://leetcode.com/problems/maximum-weight-in-two-bags/

export function maxWeight(weights: any, w1: any, w2: any): any {
    const f = Array.from({length: w1 + 1}, () => new Array(w2 + 1).fill(0));
    for (const x of weights) {
        for (let j = w1; j >= 0; j--) {
            for (let k = w2; k >= 0; k--) {
                if (x <= j) f[j][k] = Math.max(f[j][k], f[j - x][k] + x);
                if (x <= k) f[j][k] = Math.max(f[j][k], f[j][k - x] + x);
            }
        }
    }
    return f[w1][w2];
}
