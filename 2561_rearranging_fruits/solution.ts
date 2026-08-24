// LeetCode 2561 - Rearranging Fruits
// https://leetcode.com/problems/rearranging-fruits/

export function minCost(basket1: number[], basket2: number[]): number {
    const freq = new Map();
    let mn = Infinity;
    for (const x of basket1) {
        freq.set(x, (freq.get(x) || 0) + 1);
        mn = Math.min(mn, x);
    }
    for (const x of basket2) {
        freq.set(x, (freq.get(x) || 0) - 1);
        mn = Math.min(mn, x);
    }
    const extra = [];
    for (const [k, v] of freq) {
        if (v % 2 !== 0) return -1;
        for (let i = 0; i < Math.abs(v) / 2; ++i) extra.push(k);
    }
    extra.sort((a, b) => a - b);
    let ans = 0;
    for (let i = 0; i < extra.length / 2; ++i) {
        ans += Math.min(extra[i], 2 * mn);
    }
    return ans;
}
