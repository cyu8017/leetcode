// LeetCode 3670 - Maximum Product of Two Integers With No Common Bits
// https://leetcode.com/problems/maximum-product-of-two-integers-with-no-common-bits/

export function maxProduct(nums: any): any {
    let maxV = 0;
    for (const v of nums) if (v > maxV) maxV = v;
    let bitsN = 0;
    for (let x = maxV; x > 0; x >>= 1) bitsN++;
    if (bitsN === 0) bitsN = 1;
    const size = 1 << bitsN;
    const best = new Array(size).fill(0);
    for (const v of nums) if (v > best[v]) best[v] = v;
    for (let mask = 0; mask < size; mask++) {
        for (let b = 0; b < bitsN; b++) {
            if ((mask & (1 << b)) !== 0) {
                const sub = mask ^ (1 << b);
                if (best[sub] > best[mask]) best[mask] = best[sub];
            }
        }
    }
    let ans = 0;
    for (const v of nums) {
        const comp = (size - 1) ^ v;
        if (best[comp] > 0) {
            const p = v * best[comp];
            if (p > ans) ans = p;
        }
    }
    return ans;
}
