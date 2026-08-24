// LeetCode 2551 - Put Marbles in Bags
// https://leetcode.com/problems/put-marbles-in-bags/

export function putMarbles(weights: number[], k: number): number {
    const n = weights.length;
    if (k === 1 || k === n) return 0;
    const pair = new Array(n - 1);
    for (let i = 0; i < n - 1; ++i) pair[i] = weights[i] + weights[i + 1];
    pair.sort((a, b) => a - b);
    let mn = 0, mx = 0;
    for (let i = 0; i < k - 1; ++i) {
        mn += pair[i];
        mx += pair[n - 2 - i];
    }
    return mx - mn;
}
