// LeetCode 3116 - Kth Smallest Amount With Single Denomination Combination
// https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/

export function findKthSmallest(coins: number[], k: number): number {
    const gcdll = (a, b) => { while (b !== 0) { const t = a % b; a = b; b = t; } return a; };
    const lcmll = (a, b) => a / gcdll(a, b) * b;
    const bitCount = (x) => {
        let c = 0;
        while (x !== 0) { c += x & 1; x >>= 1; }
        return c;
    };
    const n = coins.length;
    const check = (mx) => {
        let cnt = 0;
        for (let i = 1; i < (1 << n); i++) {
            let v = 1;
            for (let j = 0; j < n; j++) {
                if (((i >> j) & 1) !== 0) {
                    v = lcmll(v, coins[j]);
                    if (v > mx) break;
                }
            }
            const m = bitCount(i);
            if (m % 2 === 1) cnt += Math.floor(mx / v);
            else cnt -= Math.floor(mx / v);
        }
        return cnt >= k;
    };
    let lo = 1, hi = 100000000000;
    while (lo < hi) {
        const mid = lo + Math.floor((hi - lo) / 2);
        if (check(mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
